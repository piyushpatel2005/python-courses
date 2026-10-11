from solution import *

def test_01():
    """Complete shift_totals(a) by grouping on market and shift and summing revenue."""
    _uses('shift_totals', 'groupby')
    a = pd.DataFrame({'market': ['Square', 'Square', 'Square', 'Garden'], 'shift': ['AM', 'PM', 'AM', 'PM'], 'revenue': [7, 3, 8, 2]})
    actual = shift_totals(a)
    expected = a.groupby(['market', 'shift'], observed=True, dropna=True)['revenue'].sum()
    pd.testing.assert_series_equal(actual, expected)

import ast
from pathlib import Path
import solution as _submission

def _uses(function_name, method):
    tree = ast.parse(Path(_submission.__file__).read_text())
    fn = next(node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == function_name)
    assert any(isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr == method for node in ast.walk(fn)), f"Use {method} in {function_name} to calculate the result from its input."
