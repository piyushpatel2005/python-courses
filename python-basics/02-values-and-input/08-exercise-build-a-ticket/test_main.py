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

def test_flare_count():
    """Convert the prefilled flare count"""
    assert type(flare_count) is int and flare_count == 3 and isinstance(_assignment("flare_count"), _ast.Call) and _uses_name(_assignment("flare_count"), "int") and _uses_name(_assignment("flare_count"), "flares_text"), "Use int(flares_text)"

def test_energy_cost():
    """Calculate the energy cost of three flares"""
    assert energy_cost == 18.0 and isinstance(_assignment("energy_cost"), _ast.BinOp) and isinstance(_assignment("energy_cost").op, _ast.Mult) and _uses_name(_assignment("energy_cost"), "flare_count") and _uses_name(_assignment("energy_cost"), "flare_cost"), "Multiply flare_count by flare_cost"

def test_gear_hud():
    """Format the completed gear HUD"""
    assert hud_line == "Gear for Ari: 3 flares, 18.00 energy" and isinstance(_assignment("hud_line"), _ast.JoinedStr) and all(_uses_name(_assignment("hud_line"), name) for name in ("player_text", "flare_count", "energy_cost")) and any(isinstance(n, _ast.FormattedValue) and n.format_spec is not None for n in _ast.walk(_assignment("hud_line"))), "Use an f-string and format energy_cost with :.2f"
