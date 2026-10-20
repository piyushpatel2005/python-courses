from solution import *

import ast
import contextlib
import io
import solution

# Replace only the supplied top-level fixtures; never replace learner logic.
def _variant():
    with open(solution.__file__, encoding="utf-8") as source_file:
        tree = ast.parse(source_file.read())
    replacements = {'label': 'TABLE-9'}
    for node in tree.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            name = node.targets[0].id
            if name in replacements:
                node.value = ast.parse(repr(replacements[name]), mode="eval").body
    ast.fix_missing_locations(tree)
    result = {}
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(tree, "changed_fixture.py", "exec"), result)
    return result


def _uses(technique):
    with open(solution.__file__, encoding="utf-8") as source_file:
        tree = ast.parse(source_file.read())
    for node in ast.walk(tree):
        if type(node).__name__ == technique:
            return True
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr == technique:
            return True
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == technique:
            return True
    return False

def test_01():
    """Set first_char to the first character of label."""
    assert first_char == "D", "Set first_char to the first character of label."
    assert _uses('Subscript'), "Use the requested Python technique."
    varied = _variant()
    assert eval('first_char == "T"', varied), "Check this task with a different input too."

def test_02():
    """Set last_char to the last character of label."""
    assert last_char == "7", "Set last_char to the last character of label."
    assert _uses('Subscript'), "Use the requested Python technique."
    varied = _variant()
    assert eval('last_char == "9"', varied), "Check this task with a different input too."
