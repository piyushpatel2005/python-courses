from solution import *

def test_01():
    """Return the grouped amount mean in the first tuple slot."""
    _uses('zone_metrics', 'groupby')
    a = pd.DataFrame({'zone': ['N', 'N', 'N', 'S', 'Blank'], 'amount': [3.0, 5.0, None, 1.0, None]})
    g = a.groupby('zone', observed=True, dropna=True)['amount']
    actual = zone_metrics(a)
    pd.testing.assert_series_equal(actual[0], g.mean())

def test_02():
    """Return the grouped amount sum in the second tuple slot."""
    _uses('zone_metrics', 'groupby')
    a = pd.DataFrame({'zone': ['N', 'N', 'N', 'S', 'Blank'], 'amount': [3.0, 5.0, None, 1.0, None]})
    g = a.groupby('zone', observed=True, dropna=True)['amount']
    actual = zone_metrics(a)
    pd.testing.assert_series_equal(actual[1], g.sum())

def test_03():
    """Return the grouped amount count in the third tuple slot."""
    _uses('zone_metrics', 'groupby')
    a = pd.DataFrame({'zone': ['N', 'N', 'N', 'S', 'Blank'], 'amount': [3.0, 5.0, None, 1.0, None]})
    g = a.groupby('zone', observed=True, dropna=True)['amount']
    actual = zone_metrics(a)
    pd.testing.assert_series_equal(actual[2], g.count())

def test_04():
    """Return the grouped amount size in the fourth tuple slot."""
    _uses('zone_metrics', 'groupby')
    a = pd.DataFrame({'zone': ['N', 'N', 'N', 'S', 'Blank'], 'amount': [3.0, 5.0, None, 1.0, None]})
    g = a.groupby('zone', observed=True, dropna=True)['amount']
    actual = zone_metrics(a)
    pd.testing.assert_series_equal(actual[3], g.size())

import ast
from pathlib import Path
import solution as _submission

def _uses(function_name, method):
    tree = ast.parse(Path(_submission.__file__).read_text())
    fn = next(node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == function_name)
    assert any(isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr == method for node in ast.walk(fn)), f"Use {method} in {function_name} to calculate the result from its input."
