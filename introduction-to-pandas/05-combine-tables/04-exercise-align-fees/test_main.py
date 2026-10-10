from solution import *

def test_01():
    """Complete align_fees(a, b) by concatenating columns along axis 1."""
    _uses('align_fees', 'concat')
    a = pd.DataFrame({'jars': [2, 7]}, index=['K9', 'J8'])
    b = pd.DataFrame({'fee': [3, 5]}, index=['J8', 'Q7'])
    actual = align_fees(a, b)
    expected = pd.concat([a, b], axis=1)
    pd.testing.assert_frame_equal(actual, expected)

import ast
from pathlib import Path
import solution as _submission

def _uses(function_name, method):
    tree = ast.parse(Path(_submission.__file__).read_text())
    fn = next(node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == function_name)
    assert any(isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr == method for node in ast.walk(fn)), f"Use {method} in {function_name} to calculate the result from its input."
