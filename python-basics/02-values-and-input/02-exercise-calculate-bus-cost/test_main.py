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

def test_fare_total():
    """Calculate the fare for all riders"""
    assert fare_total == 84 and isinstance(_assignment("fare_total"), _ast.BinOp) and _uses_name(_assignment("fare_total"), "fare_per_rider") and _uses_name(_assignment("fare_total"), "groups") and _uses_name(_assignment("fare_total"), "riders_per_group"), "Multiply 3 riders, 7 groups, and $4 each"

def test_open_seats():
    """Calculate the shuttle seats still free"""
    assert open_seats == 4 and isinstance(_assignment("open_seats"), _ast.BinOp) and isinstance(_assignment("open_seats").op, _ast.Sub) and _uses_name(_assignment("open_seats"), "capacity") and _uses_name(_assignment("open_seats"), "groups") and _uses_name(_assignment("open_seats"), "riders_per_group"), "Subtract 21 riders from the 25-seat capacity"
