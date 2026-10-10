from solution import *

def test_01():
    """Change average=("total", "sum") to use mean."""
    _uses('vendor_report', 'agg')
    a = pd.DataFrame({'vendor': ['Fern', 'Fern', 'Ash'], 'total': [2.0, 8.0, None]})
    actual = vendor_report(a)
    expected = a.groupby('vendor', observed=True, dropna=True).agg(average=('total', 'mean'), orders=('total', 'size'))
    pd.testing.assert_frame_equal(actual, expected)

import ast
from pathlib import Path
import solution as _submission

def _uses(function_name, method):
    tree = ast.parse(Path(_submission.__file__).read_text())
    fn = next(node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == function_name)
    assert any(isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr == method for node in ast.walk(fn)), f"Use {method} in {function_name} to calculate the result from its input."
