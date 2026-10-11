from solution import *
import solution as _solution

import ast as _ast
from pathlib import Path as _Path

def _source_tree():
    return _ast.parse(_Path(_solution.__file__).read_text())

def _assignment(name):
    for node in _source_tree().body:
        if isinstance(node, _ast.Assign) and any(isinstance(t, _ast.Name) and t.id == name for t in node.targets):
            return node.value
    raise AssertionError(f"Assign a value to {name}")

def _uses_name(node, name):
    return any(isinstance(part, _ast.Name) and part.id == name for part in _ast.walk(node))

def test_shards():
    """Use 23 shards for the lamp calculation"""
    assert shards == 23 and lamps == 5 and spare == 3 and isinstance(_assignment("lamps"), _ast.BinOp) and isinstance(_assignment("lamps").op, _ast.FloorDiv) and isinstance(_assignment("spare"), _ast.BinOp) and isinstance(_assignment("spare").op, _ast.Mod) and _uses_name(_assignment("lamps"), "shards") and _uses_name(_assignment("spare"), "shards"), "Change shards to 23 and leave the calculations intact"
