from solution import *

import ast
import contextlib
import io
import solution

# Replace only the supplied top-level fixtures; never replace learner logic.
def _variant():
    with open(solution.__file__, encoding="utf-8") as source_file:
        tree = ast.parse(source_file.read())
    replacements = {'morning_names': ['Eve', 'Eve', 'Finn', 'Gus'], 'evening_names': ['Gus', 'Hal']}
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
    """Set morning to a set of names from morning_names."""
    assert morning == {"Ada", "Bo", "Cy"}, "Set morning to a set of names from morning_names."
    assert _uses('set'), "Use the requested Python technique."
    varied = _variant()
    assert eval('morning == {"Eve", "Finn", "Gus"}', varied), "Check this task with a different input too."

def test_02():
    """Set shared to the intersection of morning and the evening names."""
    assert shared == {"Bo"}, "Set shared to the intersection of morning and the evening names."
    assert _uses('BitAnd'), "Use the requested Python technique."
    varied = _variant()
    assert eval('shared == {"Gus"}', varied), "Check this task with a different input too."

def test_03():
    """Set morning_only to the difference of the morning and evening names."""
    assert morning_only == {"Ada", "Cy"}, "Set morning_only to the difference of the morning and evening names."
    assert _uses('Sub'), "Use the requested Python technique."
    varied = _variant()
    assert eval('morning_only == {"Eve", "Finn"}', varied), "Check this task with a different input too."
