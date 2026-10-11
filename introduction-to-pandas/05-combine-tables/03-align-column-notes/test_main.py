from solution import *

def test_01():
    """Change axis=0 to axis=1 in align_notes."""
    _uses('align_notes', 'concat')
    a = pd.DataFrame({'visits': [5, 6]}, index=['Fri', 'Sat'])
    b = pd.DataFrame({'weather': ['sun', 'wind']}, index=['Sat', 'Sun'])
    actual = align_notes(a, b)
    expected = pd.concat([a, b], axis=1)
    pd.testing.assert_frame_equal(actual, expected)

import ast
from pathlib import Path
import solution as _submission

def _uses(function_name, method):
    tree = ast.parse(Path(_submission.__file__).read_text())
    fn = next(node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == function_name)
    assert any(isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr == method for node in ast.walk(fn)), f"Use {method} in {function_name} to calculate the result from its input."
