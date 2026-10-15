from solution import *


def test_01_candidate_sum() -> None:
    assert candidate_cost(4, 7) == 11
    assert candidate_cost(0, 0) == 0
    assert candidate_cost(inf, 5) == inf


def test_02_improve_distance() -> None:
    import solution
    # Supply earlier collaborators; grade only this checkpoint.
    original_candidate_cost = solution.candidate_cost
    try:
        solution.candidate_cost = lambda distance, weight: distance + weight
        d = {"a": 2, "b": 10}; p = {"a": None, "b": None}
        assert relax(d, p, "a", "b", 3) is True
        assert d == {"a": 2, "b": 5}
        assert relax(d, p, "a", "b", 3) is False
        assert relax(d, p, "a", "b", 9) is False
        assert d["b"] == 5
    finally:
        solution.candidate_cost = original_candidate_cost


def test_03_record_parent() -> None:
    import solution
    original = solution.candidate_cost
    try:
        solution.candidate_cost = lambda distance, weight: distance + weight
        d = {"a": 2, "b": 10}
        p = {"a": None, "b": "old"}
        assert relax(d, p, "a", "b", 3) is True
        assert p == {"a": None, "b": "a"}
        # An independent equal-cost fixture does not rely on task 2's update.
        d = {"a": 2, "b": 5}
        p = {"a": None, "b": "kept"}
        assert relax(d, p, "a", "b", 3) is False
        assert p["b"] == "kept"
    finally:
        solution.candidate_cost = original

