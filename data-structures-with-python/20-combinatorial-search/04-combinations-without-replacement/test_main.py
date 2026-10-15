from solution import *


def test_distinct_next_boundary():
    for i in (0, 1, 6):
        assert distinct_next(i) == i + 1


def test_distinct_leaf_snapshot():
    path = [8, 3]
    result = distinct_snapshot(path)
    assert result == (8, 3) and distinct_snapshot([]) == ()
    path.append(9)
    assert result == (8, 3), "Save values, not a mutable path reference"

    # Supply task one's boundary so this check remains independent.
    import solution as submitted

    original = submitted.distinct_next
    submitted.distinct_next = lambda index: index + 1
    try:
        assert combinations(["west", "east", "north"], 2) == [
            ("west", "east"), ("west", "north"), ("east", "north")
        ]
        assert combinations([], 0) == [()]
        assert combinations(["west"], 2) == []
    finally:
        submitted.distinct_next = original
