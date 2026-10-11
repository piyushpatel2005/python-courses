from solution import *

def test_01():
    """Change how to left in attach_areas."""
    _uses('attach_areas', 'join')
    a = pd.DataFrame({'area': ['S', 'E', 'S'], 'stall': ['A', 'B', 'C']})
    b = pd.DataFrame({'manager': ['Jo']}, index=['S'])
    actual = attach_areas(a, b)
    expected = a.set_index('area').join(b, how='left')
    pd.testing.assert_frame_equal(actual, expected)

import ast
from pathlib import Path
import solution as _submission

def _uses(function_name, method):
    tree = ast.parse(Path(_submission.__file__).read_text())
    fn = next(node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == function_name)
    assert any(isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr == method for node in ast.walk(fn)), f"Use {method} in {function_name} to calculate the result from its input."
