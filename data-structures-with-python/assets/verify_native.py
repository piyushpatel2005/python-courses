"""Audit lesson structure and run each starter/reference in isolated CPython.

Run with a Python environment containing PyYAML. Browser acceptance is separate.
"""
from __future__ import annotations

import ast
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile

import yaml

ROOT = Path(__file__).resolve().parents[1]
SCRATCH = Path.home() / '.hermes/profiles/curriculum-dev/cache/scratch/data-structures-native'


def meta(path):
    text = path.read_text()
    _, front, body = text.split('---', 2)
    return yaml.safe_load(front), body


RUNNER = r'''
import contextlib, importlib.util, io, json, pathlib, sys, traceback
base = pathlib.Path(sys.argv[1])
code = (base / 'solution.py').read_text()
output = io.StringIO()
result = {'rows': [], 'run_error': None, 'import_error': None}
try:
    with contextlib.redirect_stdout(output):
        exec(compile(code, str(base / 'solution.py'), 'exec'), {'__name__': '__main__'})
except Exception:
    result['run_error'] = traceback.format_exc()
result['stdout'] = output.getvalue()
try:
    sys.path.insert(0, str(base))
    ns = {}
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile((base / 'test_lesson.py').read_text(), str(base / 'test_lesson.py'), 'exec'), ns)
        for name, fn in list(ns.items()):
            if name.startswith('test_') and callable(fn):
                try:
                    fn()
                    result['rows'].append({'name': name, 'passed': True})
                except Exception as error:
                    result['rows'].append({'name': name, 'passed': False, 'message': str(error)})
except Exception:
    result['import_error'] = traceback.format_exc()
print(json.dumps(result))
'''


def audit():
    SCRATCH.mkdir(parents=True, exist_ok=True)
    plan = json.loads((ROOT / 'assets/curriculum-plan.json').read_text())
    expected = [ROOT / m['directory'] / l['directory'] for m in plan['modules'] for l in m['lessons']]
    found = sorted(p.parent for p in ROOT.glob('*/*/lesson.md'))
    assert set(found) == set(expected), f'Inventory differs: missing={set(expected)-set(found)}, extra={set(found)-set(expected)}'
    report = {'environment': sys.version, 'lessons': [], 'errors': [], 'quiz_questions': 0}
    for module in plan['modules']:
        questions = sorted((ROOT / module['directory'] / 'quiz').glob('q*.md'))
        assert len(questions) == 4, module['directory']
        report['quiz_questions'] += len(questions)
    for directory in expected:
        item = {'lesson': str(directory.relative_to(ROOT)), 'hashes': {}}
        try:
            fm, body = meta(directory / 'lesson.md')
            assert fm['lesson_type'] == 'coding'
            assert fm['language'] == 'python'
            assert fm['runtime'] == 'pyodide'
            assert fm['order'] == int(directory.name.split('-')[0])
            for key in ('title', 'slug', 'summary', 'seo_title', 'seo_description', 'seo_keywords'):
                assert fm.get(key), f'Missing {key}'
            section = re.search(r'^## Your Tasks?\s*\n(.*?)(?=^## |\Z)', body, re.M | re.S)
            assert section, 'Missing task section'
            tasks = re.findall(r'^\d+\.\s', section.group(1), re.M)
            tree = ast.parse((directory / 'test_main.py').read_text())
            tests = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name.startswith('test_')]
            assert len(tasks) == len(tests) > 0, f'{len(tasks)} tasks vs {len(tests)} tests'
            assert not any(isinstance(n, ast.AsyncFunctionDef) for n in tree.body)
            assert all(not n.args.args for n in tests), 'Unsupported test fixture'
            manifest = yaml.safe_load((directory / 'files.yaml').read_text())
            assert manifest['files'] == [{'path': 'main.py'}], manifest
            for filename in ('lesson.md', 'main.py', 'test_main.py', 'solution/main.py', 'files.yaml'):
                item['hashes'][filename] = hashlib.sha256((directory / filename).read_bytes()).hexdigest()
            item['task_count'] = len(tasks)
            for version, filename in [('starter', 'main.py'), ('solution', 'solution/main.py')]:
                with tempfile.TemporaryDirectory(dir=SCRATCH) as temp:
                    temp = Path(temp)
                    (temp / 'solution.py').write_text((directory / filename).read_text())
                    (temp / 'test_lesson.py').write_text((directory / 'test_main.py').read_text())
                    result = subprocess.run([sys.executable, '-B', '-c', RUNNER, str(temp)], capture_output=True, text=True, timeout=20)
                    assert result.returncode == 0, result.stderr
                    data = json.loads(result.stdout)
                    item[version] = data
                    assert not data['run_error'], f'{version} Run: {data["run_error"]}'
                    assert not data['import_error'], f'{version} Submit import: {data["import_error"]}'
                    assert len(data['rows']) == len(tasks), f'{version} rows'
                    assert all(row['passed'] == (version == 'solution') for row in data['rows']), f'{version} unexpected test vector: {data["rows"]}'
        except Exception as error:
            report['errors'].append({'lesson': item['lesson'], 'error': str(error)})
        report['lessons'].append(item)
    report['counts'] = {'lessons': len(report['lessons']), 'tasks': sum(x.get('task_count', 0) for x in report['lessons']), 'errors': len(report['errors'])}
    destination = SCRATCH / 'native-report.json'
    destination.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({'report': str(destination), 'counts': report['counts'], 'quiz_questions': report['quiz_questions'], 'errors': report['errors']}, indent=2))
    return bool(report['errors'])


if __name__ == '__main__':
    raise SystemExit(audit())
