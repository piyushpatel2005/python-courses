from solution import *

def test_01():
    """Change validate from many_to_many to many_to_one."""
    _uses('price_orders', 'merge')
    a = pd.DataFrame({'product': ['Tea', 'Tea', 'Cake'], 'units': [1, 3, 2]})
    b = pd.DataFrame({'product': ['Cake', 'Tea'], 'price': [8, 5]})
    actual = price_orders(a, b)
    expected = a.merge(b, on='product', how='left', validate='many_to_one')
    pd.testing.assert_frame_equal(actual, expected)
    try:
        price_orders(a, pd.DataFrame({'product': ['Tea', 'Tea'], 'price': [5, 6]}))
    except pd.errors.MergeError:
        pass
    else:
        assert False, 'Reject duplicate product keys in the price table.'

import ast
from pathlib import Path
import solution as _submission

def _uses(function_name, method):
    tree = ast.parse(Path(_submission.__file__).read_text())
    fn = next(node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == function_name)
    assert any(isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr == method for node in ast.walk(fn)), f"Use {method} in {function_name} to calculate the result from its input."
