from solution import *


def test_root_flags_ignore_intermediate_parents():
    d = DisjointSet(6)
    d.parent = [0, 0, 1, 3, 3, 5]
    before = d.parent[:]
    assert d.root_flags() == [True, False, False, True, False, True]
    assert d.parent == before
    assert DisjointSet(0).root_flags() == []


def test_count_boolean_roots():
    for flags, want in [
        ([], 0),
        ([True], 1),
        ([False], 0),
        ([True, False, True, True], 3),
    ]:
        assert DisjointSet.count_root_flags(flags) == want
