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

def test_heading():
    """Build the forge gear line from its values"""
    assert gear_line == "4 flares for Gear Forge" and isinstance(_assignment("gear_line"), _ast.JoinedStr) and _uses_name(_assignment("gear_line"), "flare_count") and _uses_name(_assignment("gear_line"), "forge"), "Use flare_count and forge in an f-string"

def test_payment_line():
    """Display the computed cost with two decimals"""
    assert cost_line == "Cost: $10.00" and isinstance(_assignment("cost_line"), _ast.JoinedStr) and _uses_name(_assignment("cost_line"), "cost") and any(isinstance(n, _ast.FormattedValue) and n.format_spec is not None for n in _ast.walk(_assignment("cost_line"))), "Use cost with :.2f in an f-string"
