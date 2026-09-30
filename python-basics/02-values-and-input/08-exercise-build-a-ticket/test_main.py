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

def test_ticket_count():
    """Convert the prefilled ticket count"""
    assert type(ticket_count) is int and ticket_count == 3 and isinstance(_assignment("ticket_count"), _ast.Call) and _uses_name(_assignment("ticket_count"), "int") and _uses_name(_assignment("ticket_count"), "tickets_text"), "Use int(tickets_text)"

def test_total_cost():
    """Calculate the price of three seats"""
    assert total_cost == 18.0 and isinstance(_assignment("total_cost"), _ast.BinOp) and isinstance(_assignment("total_cost").op, _ast.Mult) and _uses_name(_assignment("total_cost"), "ticket_count") and _uses_name(_assignment("total_cost"), "unit_cost"), "Multiply ticket_count by unit_cost"

def test_ticket_line():
    """Format the completed workshop ticket"""
    assert ticket_line == "Ticket for Maya: 3 seats, $18.00" and isinstance(_assignment("ticket_line"), _ast.JoinedStr) and all(_uses_name(_assignment("ticket_line"), name) for name in ("visitor_text", "ticket_count", "total_cost")) and any(isinstance(n, _ast.FormattedValue) and n.format_spec is not None for n in _ast.walk(_assignment("ticket_line"))), "Use an f-string and format total_cost with :.2f"
