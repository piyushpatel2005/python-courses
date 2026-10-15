from solution import *


def test_identify_self_link():
    d = DisjointSet(4)
    d.parent = [2, 0, 2, 3]
    assert [d.is_root(i) for i in range(4)] == [False, False, True, True]


def test_follow_valid_chain():
    d = DisjointSet(5)
    d.parent = [2, 0, 2, 4, 4]
    d.is_root = lambda i: d.parent[i] == i
    before = d.parent[:]
    assert [d.root_from(i) for i in range(5)] == [2, 2, 2, 4, 4]
    assert d.parent == before
