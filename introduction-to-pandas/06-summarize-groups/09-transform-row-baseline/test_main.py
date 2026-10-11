from solution import *

def test_01():
    """Change the operation in zone_baseline from sum to mean."""
    _uses('zone_baseline', 'transform')
    a = pd.DataFrame({'zone': ['A', 'B', 'A', 'B'], 'amount': [2.0, 6.0, 10.0, None]}, index=[7, 4, 9, 3])
    actual = zone_baseline(a)
    expected = a.groupby('zone', observed=True, dropna=True)['amount'].transform('mean')
    pd.testing.assert_series_equal(actual, expected)

import ast
from pathlib import Path
import solution as _submission

def _uses(function_name, method):
    tree = ast.parse(Path(_submission.__file__).read_text())
    fn = next(node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == function_name)
    assert any(isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr == method for node in ast.walk(fn)), f"Use {method} in {function_name} to calculate the result from its input."
