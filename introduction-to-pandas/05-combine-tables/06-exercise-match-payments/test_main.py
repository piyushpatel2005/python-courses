from solution import *

def test_01():
    """Complete match_payments(a, b) with a left merge on ticket."""
    _uses('match_payments', 'merge')
    a = pd.DataFrame({'ticket': ['Q2', 'Q3', 'Q4'], 'seats': [1, 4, 2]})
    b = pd.DataFrame({'ticket': ['Q4', 'Q2'], 'paid': [True, False]})
    actual = match_payments(a, b)
    expected = a.merge(b, on='ticket', how='left')
    pd.testing.assert_frame_equal(actual, expected)

import ast
from pathlib import Path
import solution as _submission

def _uses(function_name, method):
    tree = ast.parse(Path(_submission.__file__).read_text())
    fn = next(node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == function_name)
    assert any(isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr == method for node in ast.walk(fn)), f"Use {method} in {function_name} to calculate the result from its input."
