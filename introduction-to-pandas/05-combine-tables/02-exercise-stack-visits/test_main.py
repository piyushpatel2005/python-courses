from solution import *

def test_01():
    """Complete stack_visits(a, b) with row concatenation and a fresh index."""
    _uses('stack_visits', 'concat')
    a = pd.DataFrame({'stall': ['Birch'], 'visits': [4]}, index=[91])
    b = pd.DataFrame({'stall': ['Yew', 'Beech'], 'visits': [2, 8]}, index=[61, 74])
    actual = stack_visits(a, b)
    expected = pd.concat([a, b], ignore_index=True)
    pd.testing.assert_frame_equal(actual, expected)

import ast
from pathlib import Path
import solution as _submission

def _uses(function_name, method):
    tree = ast.parse(Path(_submission.__file__).read_text())
    fn = next(node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == function_name)
    assert any(isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr == method for node in ast.walk(fn)), f"Use {method} in {function_name} to calculate the result from its input."
