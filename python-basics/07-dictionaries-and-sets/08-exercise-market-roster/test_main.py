from solution import *

import ast
import contextlib
import io
import solution

# Replace only the supplied top-level fixtures; never replace learner logic.
def _variant():
    with open(solution.__file__, encoding="utf-8") as source_file:
        tree = ast.parse(source_file.read())
    replacements = {'discoveries': [{'location': 'Arch', 'treasure': 'gem'}, {'location': 'Vale', 'treasure': 'scroll'}, {'location': 'Arch', 'treasure': 'scroll'}, {'location': 'Dune', 'treasure': 'scroll'}], 'location': ('Hidden Annex', 'dusk')}
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
    """Loop over discoveries and append each location in discovery order to locations."""
    assert locations == ["Ridge", "Cove", "Ridge"], "Loop over discoveries and append each location in discovery order to locations."
    assert _uses('For'), "Use the requested Python technique."
    varied = _variant()
    assert eval('locations == ["Arch", "Vale", "Arch", "Dune"]', varied), "Check this task with a different input too."

def test_02():
    """Set unique_locations to a set of the locations in locations."""
    assert type(unique_locations) is set and unique_locations == {"Ridge", "Cove"}, "Set unique_locations to a set of the locations in locations."
    assert _uses('set'), "Use the requested Python technique."
    varied = _variant()
    assert eval('unique_locations == {"Arch", "Vale", "Dune"}', varied), "Check this task with a different input too."

def test_03():
    """Count each discovery treasure in treasure_counts using its current count (or zero) plus one."""
    assert treasure_counts == {"chest": 1, "compass": 2}, "Count each discovery treasure in treasure_counts using its current count (or zero) plus one."
    assert _uses('get'), "Use the requested Python technique."
    varied = _variant()
    assert eval('treasure_counts == {"gem": 1, "scroll": 3}', varied), "Check this task with a different input too."

def test_04():
    """Set report with an f-string to Map Archive at dawn: 2 places, 3 finds."""
    assert report == "Map Archive at dawn: 2 places, 3 finds", "Set report with an f-string to Map Archive at dawn: 2 places, 3 finds."
    assert _uses('JoinedStr'), "Use the requested Python technique."
    varied = _variant()
    assert eval('report == "Hidden Annex at dusk: 3 places, 4 finds"', varied), "Check this task with a different input too."
