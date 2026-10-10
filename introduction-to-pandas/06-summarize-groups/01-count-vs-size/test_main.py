from solution import *

def test_01():
    """Change the second calculation in zone_counts from count() to size()."""
    _uses('zone_counts', 'groupby')
    a = pd.DataFrame({'zone': ['East', 'East', 'West', 'West'], 'amount': [2.0, None, 4.0, None]})
    actual = zone_counts(a)
    expected = (a.groupby('zone', observed=True, dropna=True)['amount'].count(), a.groupby('zone', observed=True, dropna=True)['amount'].size())
    assert len(actual) == len(expected)
    for got, want in zip(actual, expected):
        pd.testing.assert_series_equal(got, want)

import ast
from pathlib import Path
import solution as _submission

def _uses(function_name, method):
    tree = ast.parse(Path(_submission.__file__).read_text())
    fn = next(node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == function_name)
    assert any(isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr == method for node in ast.walk(fn)), f"Use {method} in {function_name} to calculate the result from its input."
