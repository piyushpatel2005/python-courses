from solution import *

def test_01():
    """Build a zero-filled grid with repeated cells summed."""
    _uses('revenue_grid', 'pivot_table')
    a = pd.DataFrame({'zone': ['E', 'W', 'E', 'E'], 'day': ['Mon', 'Tue', 'Tue', 'Mon'], 'amount': [5.0, 9.0, 3.0, 4.0]})
    pd.testing.assert_frame_equal(revenue_grid(a), pd.pivot_table(a, index='zone', columns='day', values='amount', aggfunc='sum', fill_value=0, observed=True))

def test_02():
    """Return grouped revenue."""
    _uses('zone_report', 'agg')
    a = pd.DataFrame({'zone': ['E', 'E', 'W', 'Empty'], 'amount': [5.0, None, 9.0, None]})
    actual = zone_report(a)
    expected = a.groupby('zone', observed=True, dropna=True).agg(revenue=('amount', 'sum'))
    pd.testing.assert_series_equal(actual['revenue'], expected['revenue'])

def test_03():
    """Return grouped entries."""
    _uses('zone_report', 'agg')
    a = pd.DataFrame({'zone': ['E', 'E', 'W', 'Empty'], 'amount': [5.0, None, 9.0, None]})
    actual = zone_report(a)
    expected = a.groupby('zone', observed=True, dropna=True).agg(entries=('amount', 'size'))
    pd.testing.assert_series_equal(actual['entries'], expected['entries'])
    assert list(actual.columns) == ['revenue', 'entries'], 'Keep revenue then entries as the report columns.'

def test_04():
    """Count missing amounts independently of the pivot."""
    a = pd.DataFrame({'zone': ['E', 'W', 'E'], 'day': ['M', 'M', 'T'], 'amount': [None, 7.0, None]})
    assert missing_amounts(a) == 2, 'Count missing amount cells.'
    assert missing_amounts(a.iloc[[1]]) == 0, 'A complete row has no gaps.'

import ast
from pathlib import Path
import solution as _submission

def _uses(function_name, method):
    tree = ast.parse(Path(_submission.__file__).read_text())
    fn = next(node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == function_name)
    assert any(isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr == method for node in ast.walk(fn)), f"Use {method} in {function_name} to calculate the result from its input."
