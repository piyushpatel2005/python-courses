from solution import *

import ast
import contextlib
import io
import solution

# Replace only the supplied top-level fixtures; never replace learner logic.
def _variant():
    with open(solution.__file__, encoding="utf-8") as source_file:
        tree = ast.parse(source_file.read())
    replacements = {'exit_record': ('North Gate', '08:15')}
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
    """Set marker_name to the first element of exit_record by indexing."""
    assert marker_name == "Exit Beacon", "Set marker_name to the first element of exit_record by indexing."
    assert _uses('Subscript'), "Use the requested Python technique."
    varied = _variant()
    assert eval('marker_name == "North Gate"', varied), "Check this task with a different input too."

def test_02():
    """Unpack exit_record into marker and signal_time."""
    assert (marker, signal_time) == exit_record, "Unpack exit_record into marker and signal_time."
    source_path = solution.__file__
    assert source_path is not None
    with open(source_path, encoding="utf-8") as source_file:
        tree = ast.parse(source_file.read())
    assert any(
        isinstance(node, ast.Assign)
        and len(node.targets) == 1
        and isinstance(node.targets[0], (ast.Tuple, ast.List))
        and [part.id for part in node.targets[0].elts if isinstance(part, ast.Name)] == ["marker", "signal_time"]
        and len(node.targets[0].elts) == 2
        and isinstance(node.value, ast.Name)
        and node.value.id == "exit_record"
        for node in ast.walk(tree)
    ), "Unpack exit_record directly into marker and signal_time."
    varied = _variant()
    assert eval('(marker, signal_time) == exit_record', varied), "Check this task with a different input too."
