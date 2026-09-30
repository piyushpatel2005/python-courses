from solution import *

import ast
import contextlib
import io
import solution

# Replace only the supplied top-level fixtures; never replace learner logic.
def _variant():
    with open(solution.__file__, encoding="utf-8") as source_file:
        tree = ast.parse(source_file.read())
    replacements = {'session': ('Annex', '08:15')}
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
    """Set room_name to the first element of session by indexing."""
    assert room_name == "Studio", "Set room_name to the first element of session by indexing."
    assert _uses('Subscript'), "Use the requested Python technique."
    varied = _variant()
    assert eval('room_name == "Annex"', varied), "Check this task with a different input too."

def test_02():
    """Unpack session into room and start_time."""
    assert (room, start_time) == session, "Unpack session into room and start_time."
    assert _uses('Tuple'), "Use the requested Python technique."
    varied = _variant()
    assert eval('(room, start_time) == session', varied), "Check this task with a different input too."
