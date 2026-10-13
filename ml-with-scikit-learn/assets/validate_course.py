"""Read-only source validation; optional native execution is not browser acceptance.

Run from any directory. Dependencies: PyYAML; --run also needs the course's
scientific packages. Reports must be outside the course tree.
"""
from pathlib import Path
import argparse
import ast
import contextlib
import hashlib
import io
import json
import os
import sys
import types
import xml.etree.ElementTree as ET
import yaml

ROOT = Path(__file__).resolve().parents[1]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate(run=False):
    inventory = json.loads((ROOT / 'assets/lesson-inventory.json').read_text())
    records, figures, data_files, seen = [], [], [], set()
    assert len({item['id'] for item in inventory}) == len(inventory)
    assert {item['directory'] for item in inventory} == {
        str(path.parent.relative_to(ROOT)) for path in ROOT.glob('*/*/lesson.md')
    }, 'Lesson inventory and source directories differ'
    for item in inventory:
        folder = ROOT / item['directory']
        text = (folder / 'lesson.md').read_text()
        metadata = yaml.safe_load(text.split('---', 2)[1])
        assert all(p in seen for p in item['prerequisites']), item['id']
        seen.add(item['id'])
        assert metadata['slug'] == item['id'].split('/')[1]
        assert metadata['order'] == int(folder.name.split('-')[0])
        assert metadata['lesson_type'] == 'coding'
        manifest = yaml.safe_load((folder / 'files.yaml').read_text())['files']
        assert manifest[0]['path'] == 'main.py'
        data = manifest[1:]
        if data:
            assert text.index('## Dataset') < text.index('## Your Tasks')
            reference_manifest = yaml.safe_load((folder / 'solution/files.yaml').read_text())['files']
            assert manifest == reference_manifest
        for file in data:
            name = file['path']
            assert file['readonly'] and Path(name).suffix in ('.csv', '.json')
            assert name in text, (item['id'], name)
            assert digest(folder / name) == digest(folder / 'solution' / name)
            data_files.append(str((folder / name).relative_to(ROOT)))
        tests = (folder / 'test_main.py').read_text()
        functions = [n for n in ast.parse(tests).body
                     if isinstance(n, ast.FunctionDef) and n.name.startswith('test_')]
        assert len(functions) == 1 and not functions[0].args.args
        task_lines = [line for line in text.split('## Your Tasks')[1].splitlines()
                      if line[:1].isdigit() and '. ' in line]
        assert len(task_lines) == 1
        if item['role'] == 'demo':
            svgs = sorted(folder.glob('*.svg'))
            assert svgs, (item['id'], 'A teaching diagram is missing')
            for svg in svgs:
                tree = ET.parse(svg).getroot()
                assert all(float(v) > 0 for v in tree.attrib['viewBox'].split()[2:])
                scene = json.loads(svg.with_suffix('.excalidraw').read_text())
                assert any(e['type'] == 'text' for e in scene['elements'])
                assert not any(e['type'] == 'image' for e in scene['elements'])
                assert svg.name in text, (item['id'], 'Diagram is not linked')
                figures.append(str(svg.relative_to(ROOT)))
        record = {'id': item['id'], 'lesson_sha256': digest(folder / 'lesson.md'), 'runs': []}
        if run:
            previous = Path.cwd()
            try:
                os.chdir(folder)
                for version in ('main.py', 'solution/main.py'):
                    source = folder / version
                    buffer = io.StringIO()
                    with contextlib.redirect_stdout(buffer):
                        exec(compile(source.read_text(), str(source), 'exec'), {'__name__': '__main__'})
                        module = types.ModuleType('solution')
                        module.__file__ = str(source)
                        sys.modules['solution'] = module
                        exec(compile(source.read_text(), str(source), 'exec'), module.__dict__)
                        namespace = {}
                        exec(tests, namespace)
                        try:
                            namespace[functions[0].name]()
                            passed = True
                        except Exception as error:
                            # The actual lightweight grader also marks a raised test as failed.
                            # Import/Run errors remain outside this handler and are fatal.
                            passed = False
                            print(type(error).__name__ + ': ' + str(error))
                    assert passed == version.startswith('solution/'), (item['id'], version)
                    record['runs'].append({'version': version, 'passed': passed,
                                           'sha256': digest(source), 'stdout': buffer.getvalue()})
                    import matplotlib.pyplot as plt
                    plt.close('all')
            finally:
                os.chdir(previous)
        records.append(record)
    quizzes = sorted(ROOT.glob('*/quiz/q*.md'))
    for question in quizzes:
        metadata = yaml.safe_load(question.read_text().split('---', 2)[1])
        assert metadata['correct'] and metadata['explanation']
    expected_figures = json.loads((ROOT / 'assets/diagram-inventory.json').read_text())
    assert set(figures) == {item['svg'] for item in expected_figures}
    assert len(records) == 178 and len(quizzes) == 90
    return {'lessons': len(records), 'figures': len(figures), 'quiz_questions': len(quizzes),
            'dataset_files': len(data_files), 'native_execution': run, 'records': records}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--run', action='store_true')
    parser.add_argument('--report', type=Path)
    args = parser.parse_args()
    if args.report and args.report.resolve().is_relative_to(ROOT):
        parser.error('Keep validation reports outside the course source tree.')
    result = validate(args.run)
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(result, indent=2))
    print(json.dumps({k: v for k, v in result.items() if k != 'records'}))
