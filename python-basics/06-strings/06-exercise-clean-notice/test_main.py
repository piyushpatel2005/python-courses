from solution import *

import ast
import contextlib
import io
import solution

# Replace only the supplied top-level fixtures; never replace learner logic.
def _variant(raw_notice='  SHOP BUSY  '):
    with open(solution.__file__, encoding="utf-8") as source_file:
        tree = ast.parse(source_file.read())
    replacements = {'raw_notice': raw_notice}
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
    """Set notice to the stripped, lowercased raw_notice."""
    assert notice == "shop closed", "Set notice to the stripped, lowercased raw_notice."
    assert _uses('strip'), "Use the requested Python technique."
    varied = _variant()
    assert eval('notice == "shop busy"', varied), "Check this task with a different input too."

def test_02():
    """Set updated_notice to notice with closed replaced by open."""
    assert updated_notice == "shop open", "Set updated_notice to notice with closed replaced by open."
    assert _uses('replace'), "Use the requested Python technique."
    varied = _variant()
    assert eval('updated_notice == "shop busy"', varied), "Check this task with a different input too."

def test_03():
    """Set is_shop_notice to whether notice starts with shop."""
    assert is_shop_notice is True, "Set is_shop_notice to whether notice starts with shop."
    assert _uses('startswith'), "Use the requested Python technique."
    varied = _variant()
    assert eval('is_shop_notice is True', varied), "Check this task with a different input too."
    other_notice = _variant('  OFFICE CLOSED  ')
    assert other_notice.get('is_shop_notice') is False, "A notice starting with office is not a shop notice; check the prefix shop."
