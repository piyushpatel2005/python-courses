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
    """Build the invoice heading from its values"""
    assert heading == "4 posters for the art fair" and isinstance(_assignment("heading"), _ast.JoinedStr) and _uses_name(_assignment("heading"), "quantity") and _uses_name(_assignment("heading"), "event"), "Use quantity and event in an f-string"

def test_payment_line():
    """Display the computed total with two decimals"""
    assert payment_line == "Due: $10.00" and isinstance(_assignment("payment_line"), _ast.JoinedStr) and _uses_name(_assignment("payment_line"), "total") and any(isinstance(n, _ast.FormattedValue) and n.format_spec is not None for n in _ast.walk(_assignment("payment_line"))), "Use total with :.2f in an f-string"
