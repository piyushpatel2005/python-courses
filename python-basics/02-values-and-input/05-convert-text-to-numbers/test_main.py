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

def test_order_text():
    """Convert the updated order text to calculate 17 shards"""
    assert shard_text == "15" and shards == 17 and any(isinstance(n, _ast.Call) and isinstance(n.func, _ast.Name) and n.func.id == "int" and _uses_name(n, "shard_text") for n in _ast.walk(_assignment("shards"))), "Change the quoted number to '15'"
