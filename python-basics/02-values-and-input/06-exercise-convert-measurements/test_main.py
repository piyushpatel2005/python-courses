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

def test_tray_count():
    """Parse whole-number tray text"""
    assert type(tray_count) is int and tray_count == 9 and isinstance(_assignment("tray_count"), _ast.Call) and _uses_name(_assignment("tray_count"), "int") and _uses_name(_assignment("tray_count"), "tray_text"), "Use int(tray_text)"

def test_liters_per_tray():
    """Parse decimal measurement text"""
    assert type(liters_per_tray) is float and liters_per_tray == 1.5 and isinstance(_assignment("liters_per_tray"), _ast.Call) and _uses_name(_assignment("liters_per_tray"), "float") and _uses_name(_assignment("liters_per_tray"), "liters_text"), "Use float(liters_text)"
