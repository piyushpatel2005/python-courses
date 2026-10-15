from solution import *


def test_01_zero_is_reachable() -> None:
    assert reachable(0) is True
    assert reachable(7) is True
    assert reachable(inf) is False
    g = {"a": [("b", 0)], "b": [("a", 0), ("c", 0)], "c": []}
    assert route_status(g, "a", "c") == (0, ["a", "b", "c"])


def test_02_unreachable_marker() -> None:
    import solution
    # Supply earlier collaborators; grade only this checkpoint.
    original_reachable = solution.reachable
    try:
        solution.reachable = lambda distance: distance != inf
        g = {"a": [("b", 0)], "b": [], "island": []}
        assert route_status(g, "a", "island") == (None, [])
        assert route_status(g, "a", "a") == (0, ["a"])
        assert g["a"] == [("b", 0)]
    finally:
        solution.reachable = original_reachable

