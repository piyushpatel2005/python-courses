from solution import *
import solution as _solution

import ast as _ast
from pathlib import Path as _Path

def _assignment(name):
    tree = _ast.parse(_Path(_solution.__file__).read_text())
    for node in tree.body:
        if isinstance(node, _ast.Assign) and any(isinstance(target, _ast.Name) and target.id == name for target in node.targets):
            return node.value
    raise AssertionError(f"Assign a value to {name}")

def _uses_name(expr, name):
    return any(isinstance(node, _ast.Name) and node.id == name for node in _ast.walk(expr))

def test_cell_count():
    """Parse whole-number cell text"""
    assert type(cell_count) is int and cell_count == 9 and isinstance(_assignment("cell_count"), _ast.Call) and _uses_name(_assignment("cell_count"), "int") and _uses_name(_assignment("cell_count"), "cell_text"), "Use int(cell_text)"

def test_charge_per_cell():
    """Parse decimal charge text"""
    assert type(charge_per_cell) is float and charge_per_cell == 1.5 and isinstance(_assignment("charge_per_cell"), _ast.Call) and _uses_name(_assignment("charge_per_cell"), "float") and _uses_name(_assignment("charge_per_cell"), "charge_text"), "Use float(charge_text)"
