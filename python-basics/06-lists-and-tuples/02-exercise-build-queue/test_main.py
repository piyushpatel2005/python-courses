from solution import *

import ast
import contextlib
import io
import solution

# Replace only the supplied top-level fixtures; never replace learner logic.
def _variant():
    with open(solution.__file__, encoding="utf-8") as source_file:
        tree = ast.parse(source_file.read())
    replacements = {'queue': ['Pia', 'Ray', 'Tao']}
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
    """Set queue to a list containing Uma, Jae, Sol in that order."""
    assert queue == ["Uma", "Jae", "Sol"], "Set queue to a list containing Uma, Jae, Sol in that order."
    assert _uses('List'), "Use the requested Python technique."
    varied = _variant()
    assert eval('queue == ["Pia", "Ray", "Tao"]', varied), "Check this task with a different input too."

def test_02():
    """Set next_person to the first item of queue."""
    assert next_person == "Uma", "Set next_person to the first item of queue."
    assert _uses('Subscript'), "Use the requested Python technique."
    varied = _variant()
    assert eval('next_person == "Pia"', varied), "Check this task with a different input too."

def test_03():
    """Set last_person to the last item of queue."""
    assert last_person == "Sol", "Set last_person to the last item of queue."
    assert _uses('Subscript'), "Use the requested Python technique."
    varied = _variant()
    assert eval('last_person == "Tao"', varied), "Check this task with a different input too."
