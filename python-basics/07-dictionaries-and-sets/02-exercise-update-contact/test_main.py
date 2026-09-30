from solution import *

import ast
import contextlib
import io
import solution

# Replace only the supplied top-level fixtures; never replace learner logic.
def _variant():
    with open(solution.__file__, encoding="utf-8") as source_file:
        tree = ast.parse(source_file.read())
    replacements = {'contact': {'name': 'Zed', 'visits': 7}}
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
    """Set visitor to the value under name in contact."""
    assert visitor == "Ivy", "Set visitor to the value under name in contact."
    assert _uses('Subscript'), "Use the requested Python technique."
    varied = _variant()
    assert eval('visitor == "Zed"', varied), "Check this task with a different input too."

def test_02():
    """Update contact['visits'] to 3."""
    assert contact["visits"] == 3, "Update contact['visits'] to 3."
    assert _uses('Subscript'), "Use the requested Python technique."
    varied = _variant()
    assert eval('contact["visits"] == 3', varied), "Check this task with a different input too."

def test_03():
    """Set phone with contact.get('phone', 'not provided')."""
    assert phone == "not provided", "Set phone with contact.get('phone', 'not provided')."
    assert _uses('get'), "Use the requested Python technique."
    varied = _variant()
    assert eval('phone == "not provided"', varied), "Check this task with a different input too."
