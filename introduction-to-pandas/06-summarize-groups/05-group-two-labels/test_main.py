from solution import *

def test_01():
    """Change the grouping key in daily_gifts to ["zone", "day"]."""
    _uses('daily_gifts', 'groupby')
    a = pd.DataFrame({'zone': ['East', 'East', 'East', 'West'], 'day': ['Mon', 'Tue', 'Mon', 'Mon'], 'amount': [2, 4, 3, 9]})
    actual = daily_gifts(a)
    expected = a.groupby(['zone', 'day'], observed=True, dropna=True)['amount'].sum()
    pd.testing.assert_series_equal(actual, expected)

import ast
from pathlib import Path
import solution as _submission

def _uses(function_name, method):
    tree = ast.parse(Path(_submission.__file__).read_text())
    fn = next(node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == function_name)
    assert any(isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr == method for node in ast.walk(fn)), f"Use {method} in {function_name} to calculate the result from its input."
