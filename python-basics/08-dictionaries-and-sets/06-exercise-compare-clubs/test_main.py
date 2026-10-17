from solution import *

import ast
import contextlib
import io
import solution

# Replace only the supplied top-level fixtures; never replace learner logic.
def _variant():
    with open(solution.__file__, encoding="utf-8") as source_file:
        tree = ast.parse(source_file.read())
    replacements = {'ari_stops': ['Arch', 'Arch', 'Vale', 'Pass'], 'scout_stops': ['Pass', 'Dune']}
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
    """Set ari_route to a set of names from ari_stops."""
    assert ari_route == {"Ridge", "Cove", "Grove"}, "Set ari_route to a set of names from ari_stops."
    assert _uses('set'), "Use the requested Python technique."
    varied = _variant()
    assert eval('ari_route == {"Arch", "Vale", "Pass"}', varied), "Check this task with a different input too."

def test_02():
    """Set overlap to the intersection of ari_route and the scout_stops."""
    assert overlap == {"Cove"}, "Set overlap to the intersection of ari_route and the scout_stops."
    assert _uses('BitAnd'), "Use the requested Python technique."
    varied = _variant()
    assert eval('overlap == {"Pass"}', varied), "Check this task with a different input too."

def test_03():
    """Set ari_only to the difference of the ari_route and scout_stops."""
    assert ari_only == {"Ridge", "Grove"}, "Set ari_only to the difference of the ari_route and scout_stops."
    assert _uses('Sub'), "Use the requested Python technique."
    varied = _variant()
    assert eval('ari_only == {"Arch", "Vale"}', varied), "Check this task with a different input too."
