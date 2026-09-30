from solution import *

import ast
import contextlib
import io
import solution

# Replace only the supplied top-level fixtures; never replace learner logic.
def _variant():
    with open(solution.__file__, encoding="utf-8") as source_file:
        tree = ast.parse(source_file.read())
    replacements = {'signups': [{'name': 'Mia', 'activity': 'bread'}, {'name': 'Oli', 'activity': 'jam'}, {'name': 'Mia', 'activity': 'jam'}, {'name': 'Pam', 'activity': 'jam'}], 'location': ('South Shed', '11:30')}
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
    """Loop over signups and append each name in signup order to names."""
    assert names == ["Lia", "Ren", "Lia"], "Loop over signups and append each name in signup order to names."
    assert _uses('For'), "Use the requested Python technique."
    varied = _variant()
    assert eval('names == ["Mia", "Oli", "Mia", "Pam"]', varied), "Check this task with a different input too."

def test_02():
    """Set unique_names to a set of the names in names."""
    assert type(unique_names) is set and unique_names == {"Lia", "Ren"}, "Set unique_names to a set of the names in names."
    assert _uses('set'), "Use the requested Python technique."
    varied = _variant()
    assert eval('unique_names == {"Mia", "Oli", "Pam"}', varied), "Check this task with a different input too."

def test_03():
    """Count each signup activity in activity_counts using its current count (or zero) plus one."""
    assert activity_counts == {"seeds": 1, "tools": 2}, "Count each signup activity in activity_counts using its current count (or zero) plus one."
    assert _uses('get'), "Use the requested Python technique."
    varied = _variant()
    assert eval('activity_counts == {"bread": 1, "jam": 3}', varied), "Check this task with a different input too."

def test_04():
    """Set report with an f-string to Market Hall at 10:00: 2 people, 3 bookings."""
    assert report == "Market Hall at 10:00: 2 people, 3 bookings", "Set report with an f-string to Market Hall at 10:00: 2 people, 3 bookings."
    assert _uses('JoinedStr'), "Use the requested Python technique."
    varied = _variant()
    assert eval('report == "South Shed at 11:30: 3 people, 4 bookings"', varied), "Check this task with a different input too."
