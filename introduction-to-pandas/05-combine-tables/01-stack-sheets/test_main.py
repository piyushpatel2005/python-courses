from solution import *

def test_01():
    """Change ignore_index to True in stack_sheets."""
    _uses('stack_sheets', 'concat')
    a = pd.DataFrame({'stall': ['Oak'], 'crates': [7]}, index=[12])
    b = pd.DataFrame({'stall': ['Pine', 'Elm'], 'crates': [4, 9]}, index=[41, 43])
    actual = stack_sheets(a, b)
    expected = pd.concat([a, b], ignore_index=True)
    pd.testing.assert_frame_equal(actual, expected)

import ast
from pathlib import Path
import solution as _submission

def _uses(function_name, method):
    tree = ast.parse(Path(_submission.__file__).read_text())
    fn = next(node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == function_name)
    assert any(isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr == method for node in ast.walk(fn)), f"Use {method} in {function_name} to calculate the result from its input."
