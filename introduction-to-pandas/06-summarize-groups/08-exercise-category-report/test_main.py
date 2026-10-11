from solution import *

def test_01():
    """Return grouped revenue."""
    _uses('category_report', 'agg')
    a = pd.DataFrame({'category': ['E', 'E', 'W', 'Empty'], 'amount': [5.0, None, 9.0, None]})
    actual = category_report(a)
    expected = a.groupby('category', observed=True, dropna=True).agg(revenue=('amount', 'sum'))
    pd.testing.assert_series_equal(actual['revenue'], expected['revenue'])

def test_02():
    """Return grouped entries."""
    _uses('category_report', 'agg')
    a = pd.DataFrame({'category': ['E', 'E', 'W', 'Empty'], 'amount': [5.0, None, 9.0, None]})
    actual = category_report(a)
    expected = a.groupby('category', observed=True, dropna=True).agg(entries=('amount', 'size'))
    pd.testing.assert_series_equal(actual['entries'], expected['entries'])
    assert list(actual.columns) == ['revenue', 'entries'], 'Keep revenue then entries as the report columns.'

import ast
from pathlib import Path
import solution as _submission

def _uses(function_name, method):
    tree = ast.parse(Path(_submission.__file__).read_text())
    fn = next(node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == function_name)
    assert any(isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr == method for node in ast.walk(fn)), f"Use {method} in {function_name} to calculate the result from its input."
