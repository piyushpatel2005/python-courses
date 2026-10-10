from solution import *

def test_01():
    """Add fill_value=0 to daily_grid."""
    _uses('daily_grid', 'pivot_table')
    a = pd.DataFrame({'zone': ['E', 'E', 'W', 'E'], 'day': ['Mon', 'Tue', 'Tue', 'Mon'], 'amount': [2, 3, 4, 5]})
    actual = daily_grid(a)
    expected = pd.pivot_table(a, index='zone', columns='day', values='amount', aggfunc='sum', fill_value=0, observed=True)
    pd.testing.assert_frame_equal(actual, expected)

import ast
from pathlib import Path
import solution as _submission

def _uses(function_name, method):
    tree = ast.parse(Path(_submission.__file__).read_text())
    fn = next(node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == function_name)
    assert any(isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr == method for node in ast.walk(fn)), f"Use {method} in {function_name} to calculate the result from its input."
