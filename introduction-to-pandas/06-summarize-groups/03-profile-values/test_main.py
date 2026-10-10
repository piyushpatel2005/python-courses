from solution import *

def test_01():
    """Change dropna=True to dropna=False in profile_sales."""
    _uses('profile_sales', 'value_counts')
    a = pd.DataFrame({'category': ['Repair', None, 'Repair', 'Plant', None], 'amount': [2.0, None, 6.0, 10.0, 14.0]})
    actual = profile_sales(a)
    expected = (a['amount'].describe(), a['category'].value_counts(dropna=False))
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
