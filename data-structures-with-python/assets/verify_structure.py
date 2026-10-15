"""Source and diagram integrity checks; runtime acceptance is separate.

Run with a Python containing PyYAML. Reports every missing planned artifact.
"""
from __future__ import annotations

import ast
import hashlib
import json
from pathlib import Path
import re
import sys

import yaml

ROOT = Path(__file__).resolve().parents[1]
OUT = Path.home() / '.hermes/profiles/curriculum-dev/cache/scratch/data-structures-validation'


def frontmatter(path: Path) -> tuple[dict, str]:
    _, header, body = path.read_text().split('---', 2)
    return yaml.safe_load(header), body


def audit() -> int:
    plan = json.loads((ROOT / 'assets/curriculum-plan.json').read_text())
    diagrams = json.loads((ROOT / 'assets/diagram-plan.json').read_text())
    diagrams += json.loads((ROOT / 'assets/additional-diagram-plan.json').read_text())
    errors: list[str] = []
    annotation_gaps: list[dict] = []
    source_files: dict[str, str] = {}
    annotated = functions = parameters = annotated_parameters = 0
    expected_lessons: list[Path] = []
    for module in plan['modules']:
        for lesson in module['lessons']:
            directory = ROOT / module['directory'] / lesson['directory']
            expected_lessons.append(directory / 'lesson.md')
            try:
                meta, body = frontmatter(directory / 'lesson.md')
                assert meta['slug'] == lesson['slug']
                assert meta['order'] == lesson['order']
                assert meta['runtime'] == 'pyodide'
                assert meta['language'] == 'python'
                assert meta['lesson_type'] == 'coding'
                for filename in ('lesson.md', 'main.py', 'solution/main.py', 'test_main.py', 'files.yaml'):
                    path = directory / filename
                    text = path.read_text()
                    source_files[str(path.relative_to(ROOT))] = hashlib.sha256(path.read_bytes()).hexdigest()
                    assert not re.search(r'leetcode|hackerrank|codewars|fullstack\.io|javascript|the supplied (?:book|pdf)', text, re.I), f'Reference-platform mention in {filename}'
                for filename in ('main.py', 'solution/main.py'):
                    tree = ast.parse((directory / filename).read_text())
                    for node in ast.walk(tree):
                        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                            if node.name.startswith('_') and not node.name.startswith('__'):
                                continue
                            functions += 1
                            args = [a for a in node.args.posonlyargs + node.args.args + node.args.kwonlyargs if a.arg not in ('self', 'cls')]
                            args += [a for a in (node.args.vararg, node.args.kwarg) if a is not None]
                            parameters += len(args)
                            annotated_parameters += sum(a.annotation is not None for a in args)
                            annotated += node.returns is not None
                            missing = [a.arg for a in args if a.annotation is None]
                            if node.returns is None:
                                missing.append('return')
                            if missing:
                                annotation_gaps.append({'file': str((directory / filename).relative_to(ROOT)), 'function': node.name, 'missing': missing})
            except Exception as error:
                errors.append(f'{directory.relative_to(ROOT)}: {error}')
        for question in sorted((ROOT / module['directory'] / 'quiz').glob('q*.md')):
            if re.search(r'leetcode|hackerrank|codewars|fullstack\.io|javascript', question.read_text(), re.I):
                errors.append(f'Reference-platform mention in {question.relative_to(ROOT)}')
    discovered = set(ROOT.glob('*/*/lesson.md'))
    for path in discovered.symmetric_difference(expected_lessons):
        errors.append(f'Lesson inventory mismatch: {path.relative_to(ROOT)}')
    assert len({row['lesson'] for row in diagrams}) == len(diagrams), 'Duplicate diagram lesson assignment'
    assert len({row['file'] for row in diagrams}) == len(diagrams), 'Duplicate diagram filename'
    for row in diagrams:
        try:
            directory = ROOT / row['lesson']
            for name in (row['file'], row['editable']):
                canonical = ROOT / 'assets/diagrams' / name
                local = directory / name
                assert canonical.read_bytes() == local.read_bytes(), f'Canonical/local mismatch: {name}'
                assert local.stat().st_size > 100, f'Empty figure: {name}'
                source_files[str(local.relative_to(ROOT))] = hashlib.sha256(local.read_bytes()).hexdigest()
            body = (directory / 'lesson.md').read_text()
            assert re.search(r'!\[([^\n]+?)\]\(' + re.escape(row['file']) + r'\)', body), 'Missing diagram Markdown or alt text'
            scene = json.loads((directory / row['editable']).read_text())
            assert scene['type'] == 'excalidraw'
            elements = [e for e in scene['elements'] if not e.get('isDeleted')]
            assert any(e['type'] == 'text' for e in elements)
            assert any(e['type'] in ('rectangle', 'ellipse', 'diamond') for e in elements)
            assert not any(e['type'] == 'image' for e in elements), 'Flattened image is not an editable diagram'
        except Exception as error:
            errors.append(f'Diagram {row["file"]}: {error}')
    OUT.mkdir(parents=True, exist_ok=True)
    report = {'lessons': len(expected_lessons), 'diagrams': len(diagrams), 'functions': functions,
              'annotated_returns': annotated, 'parameters': parameters, 'annotated_parameters': annotated_parameters,
              'annotation_gaps': annotation_gaps, 'errors': errors, 'source_hashes': source_files,
              'note': 'Scene checks are structural only; actual editor import/edit/export and visual evidence are separately required.'}
    (OUT / 'structure-report.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({k: v for k, v in report.items() if k != 'source_hashes'}, indent=2))
    return bool(errors or annotation_gaps)


if __name__ == '__main__':
    sys.exit(audit())
