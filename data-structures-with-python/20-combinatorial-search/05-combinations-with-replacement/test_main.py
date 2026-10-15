from solution import *


def test_repeated_next_boundary():
    for i in (0, 1, 6):
        assert repeated_next(i) == i


def test_repeated_leaf_snapshot():
    path = [8, 3]
    result = repeated_snapshot(path)
    assert result == (8, 3) and repeated_snapshot([]) == ()
    path.append(9)
    assert result == (8, 3), "Save values, not a mutable path reference"

    # Supply task one's boundary so this check remains independent.
    import solution as submitted

    original = submitted.repeated_next
    submitted.repeated_next = lambda index: index
    try:
        assert combinations_repeated(["west", "east", "north"], 2) == [
            ("west", "west"), ("west", "east"), ("west", "north"),
            ("east", "east"), ("east", "north"), ("north", "north"),
        ]
        assert combinations_repeated([], 0) == [()]
        assert combinations_repeated([], 2) == []
    finally:
        submitted.repeated_next = original
