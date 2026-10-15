from solution import *


def test_01_active_color() -> None:
    assert is_active(1) is True
    assert is_active(0) is False and is_active(2) is False


def test_02_finish_not_cycle() -> None:
    import solution
    # Supply earlier collaborators; grade only this checkpoint.
    original_is_active = solution.is_active
    try:
        solution.is_active = lambda color: color == 1
        diamond = {"s": ["a", "b"], "a": ["t"], "b": ["t"], "t": []}
        assert not directed_cycle(diamond)
        assert directed_cycle({"a": ["b"], "b": ["a"]})
        assert directed_cycle({"idle": [], "x": ["x"]})
        assert not directed_cycle({})
    finally:
        solution.is_active = original_is_active

