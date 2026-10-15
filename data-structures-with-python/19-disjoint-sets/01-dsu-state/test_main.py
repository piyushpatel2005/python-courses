from solution import *


def test_validate_component_size():
    assert DisjointSet.validate_size(0) is None and DisjointSet.validate_size(5) is None
    for bad in (-1, True, 2.5):
        try:
            DisjointSet.validate_size(bad)
        except ValueError:
            pass
        else:
            assert False, "Reject invalid n"


def test_parent_initialization():
    for n in (0, 1, 5):
        assert DisjointSet.initial_parents(n) == list(range(n))
    first = DisjointSet.initial_parents(3)
    second = DisjointSet.initial_parents(3)
    first[0] = 2
    assert second == [0, 1, 2]


def test_initial_size_list():
    assert DisjointSet.initial_sizes(0) == []
    first = DisjointSet.initial_sizes(3)
    second = DisjointSet.initial_sizes(3)
    assert first == [1, 1, 1] and second == [1, 1, 1]
    first[0] = 7
    assert second == [1, 1, 1], "Each size list must be independent"
