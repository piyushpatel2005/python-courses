from solution import *

def test_01():
    """Left-join fees using band as the left index."""
    _uses('attach_bands', 'join')
    a = pd.DataFrame({'band': ['C', 'D', 'C'], 'tables': [2, 1, 4]})
    b = pd.DataFrame({'fee': [8]}, index=['C'])
    actual = attach_bands(a, b)
    expected = a.set_index('band').join(b, how='left')
    pd.testing.assert_frame_equal(actual, expected)

def test_02():
    """Reject repeated fee-band lookup labels."""
    a = pd.DataFrame({'band': ['C', 'D'], 'tables': [2, 1]})
    try:
        attach_bands(a, pd.DataFrame({'fee': [8, 9]}, index=['C', 'C']))
    except ValueError:
        pass
    else:
        assert False, 'Reject repeated lookup keys.'

import ast
from pathlib import Path
import solution as _submission

def _uses(function_name, method):
    tree = ast.parse(Path(_submission.__file__).read_text())
    fn = next(node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == function_name)
    assert any(isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr == method for node in ast.walk(fn)), f"Use {method} in {function_name} to calculate the result from its input."
