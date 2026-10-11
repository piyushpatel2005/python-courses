from solution import *

def test_01():
    """Complete visit_difference(a) using groupby(...).transform("mean") to subtract each category baseline."""
    _uses('visit_difference', 'transform')
    a = pd.DataFrame({'category': ['Book', 'Food', 'Book', 'Food'], 'visitors': [3.0, 10.0, 9.0, 18.0]}, index=[8, 2, 6, 4])
    actual = visit_difference(a)
    expected = a['visitors'] - a.groupby('category', observed=True, dropna=True)['visitors'].transform('mean')
    pd.testing.assert_series_equal(actual, expected)

import ast
from pathlib import Path
import solution as _submission

def _uses(function_name, method):
    tree = ast.parse(Path(_submission.__file__).read_text())
    fn = next(node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == function_name)
    assert any(isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr == method for node in ast.walk(fn)), f"Use {method} in {function_name} to calculate the result from its input."
