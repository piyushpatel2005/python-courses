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

def test_points_needed():
    """Calculate the energy for all cache points"""
    assert points_needed == 84 and isinstance(_assignment("points_needed"), _ast.BinOp) and _uses_name(_assignment("points_needed"), "points_per_coin") and _uses_name(_assignment("points_needed"), "chests") and _uses_name(_assignment("points_needed"), "coins_per_chest"), "Multiply 3 points per cache, 7 chests, and 4 energy each"

def test_open_slots():
    """Calculate the pack slots still free"""
    assert open_slots == 4 and isinstance(_assignment("open_slots"), _ast.BinOp) and isinstance(_assignment("open_slots").op, _ast.Sub) and _uses_name(_assignment("open_slots"), "pack_slots") and _uses_name(_assignment("open_slots"), "chests") and _uses_name(_assignment("open_slots"), "coins_per_chest"), "Subtract 21 points from the 25 pack slots"
