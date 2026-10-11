from solution import *

import ast
import contextlib
import io
import solution

# Replace only the supplied top-level fixtures; never replace learner logic.
def _variant(with_clue=False):
    with open(solution.__file__, encoding="utf-8") as source_file:
        tree = ast.parse(source_file.read())
    alternate = {'landmark': 'Amber Steps', 'marks': 7}
    if with_clue:
        alternate['clue'] = 'under the arch'
    replacements = {'map_entry': alternate}
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
    """Set landmark to the value under landmark in map_entry."""
    assert landmark == "Moss Gate", "Set landmark to the value under landmark in map_entry."
    assert _uses('Subscript'), "Use the requested Python technique."
    varied = _variant()
    assert eval('landmark == "Amber Steps"', varied), "Check this task with a different input too."

def test_02():
    """Update map_entry['marks'] to 3."""
    assert map_entry["marks"] == 3, "Update map_entry['marks'] to 3."
    assert _uses('Subscript'), "Use the requested Python technique."
    varied = _variant()
    assert eval('map_entry["marks"] == 3', varied), "Check this task with a different input too."

def test_03():
    """Set clue with map_entry.get('clue', 'unmarked')."""
    assert clue == "unmarked", "Set clue with map_entry.get('clue', 'unmarked')."
    source_path = solution.__file__
    assert source_path is not None
    with open(source_path, encoding="utf-8") as source_file:
        tree = ast.parse(source_file.read())
    assert any(
        isinstance(node, ast.Assign)
        and len(node.targets) == 1
        and isinstance(node.targets[0], ast.Name)
        and node.targets[0].id == 'clue'
        and isinstance(node.value, ast.Call)
        and isinstance(node.value.func, ast.Attribute)
        and isinstance(node.value.func.value, ast.Name)
        and node.value.func.value.id == 'map_entry'
        and node.value.func.attr == 'get'
        and len(node.value.args) == 2
        and all(isinstance(arg, ast.Constant) and arg.value == expected
                for arg, expected in zip(node.value.args, ['clue', 'unmarked']))
        for node in ast.walk(tree)
    ), "Assign map_entry.get('clue', 'unmarked') to clue."
    varied = _variant(with_clue=True)
    assert eval('clue == "under the arch"', varied), "Use the stored clue when the key exists."
