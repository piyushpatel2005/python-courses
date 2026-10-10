from solution import *

def test_01():
    """Change how="inner" to how="left" in attach_vendors."""
    _uses('attach_vendors', 'merge')
    a = pd.DataFrame({'stall': ['C4', 'X0', 'B1'], 'tables': [1, 3, 2]})
    b = pd.DataFrame({'stall': ['B1', 'C4'], 'vendor': ['Zed', 'Ivy']})
    actual = attach_vendors(a, b)
    expected = a.merge(b, on='stall', how='left')
    pd.testing.assert_frame_equal(actual, expected)

import ast
from pathlib import Path
import solution as _submission

def _uses(function_name, method):
    tree = ast.parse(Path(_submission.__file__).read_text())
    fn = next(node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == function_name)
    assert any(isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr == method for node in ast.walk(fn)), f"Use {method} in {function_name} to calculate the result from its input."
