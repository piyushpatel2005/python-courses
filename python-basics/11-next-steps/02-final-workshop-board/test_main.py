import ast
import inspect
import textwrap
from solution import reserved_total, available_places, build_board


def test_reserved_total():
    assert reserved_total([2, 1, 4]) == 7
    assert reserved_total([8, 1]) == 9
    assert reserved_total([]) == 0
    tree = ast.parse(textwrap.dedent(inspect.getsource(reserved_total)))
    assert any(isinstance(node, ast.For) for node in ast.walk(tree)), "Use the requested loop, not sum()."


def test_available_places():
    assert available_places(7, 2) == 5
    assert available_places(2, 4) == 0
    assert available_places(5, 5) == 0


def test_build_board():
    sessions = [
        {"name": "Printing", "capacity": 4, "reservations": [1, 2]},
        {"name": "Sewing", "capacity": 2, "reservations": [2, 1]},
        {"name": "Empty", "capacity": 6, "reservations": []},
    ]
    assert build_board(sessions) == ["Printing: 3 reserved, 1 available", "Sewing: 3 reserved, 0 available", "Empty: 0 reserved, 6 available"]
    assert build_board([]) == []
    # Replace the two helpers temporarily: a recomputation in build_board will fail.
    namespace = build_board.__globals__
    original_total = namespace["reserved_total"]
    original_available = namespace["available_places"]
    try:
        namespace["reserved_total"] = lambda numbers: 7
        namespace["available_places"] = lambda capacity, reserved: 1 if reserved == 7 else -99
        assert build_board([{"name": "Probe", "capacity": 30, "reservations": [2]}]) == ["Probe: 7 reserved, 1 available"], "Reuse both supplied helpers inside build_board."
    finally:
        namespace["reserved_total"] = original_total
        namespace["available_places"] = original_available
