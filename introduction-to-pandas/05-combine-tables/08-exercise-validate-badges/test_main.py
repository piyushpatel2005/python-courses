from solution import *

def test_01():
    """Complete audit_badges(a, b) with an inner merge on badge and validate="one_to_one"."""
    _uses('audit_badges', 'merge')
    a = pd.DataFrame({'badge': ['P7', 'P8', 'P9'], 'time': [8, 9, 10]})
    b = pd.DataFrame({'badge': ['P8', 'P7'], 'name': ['Lin', 'Kim']})
    actual = audit_badges(a, b)
    expected = a.merge(b, on='badge', how='inner')
    pd.testing.assert_frame_equal(actual, expected)
    for left, right in [(pd.concat([a, a.iloc[[0]]], ignore_index=True), b), (a, pd.concat([b, b.iloc[[0]]], ignore_index=True))]:
        try:
            audit_badges(left, right)
        except pd.errors.MergeError:
            pass
        else:
            assert False, 'Reject duplicate keys on either side.'

import ast
from pathlib import Path
import solution as _submission

def _uses(function_name, method):
    tree = ast.parse(Path(_submission.__file__).read_text())
    fn = next(node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == function_name)
    assert any(isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr == method for node in ast.walk(fn)), f"Use {method} in {function_name} to calculate the result from its input."
