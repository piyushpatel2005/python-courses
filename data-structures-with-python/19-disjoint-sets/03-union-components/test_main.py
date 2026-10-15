from solution import *


def test_resolve_union_endpoints():
    d = DisjointSet(5)
    d.parent = [0, 0, 1, 3, 3]
    before = d.parent[:]
    assert d.union_roots(2, 4) == (0, 3)
    assert d.parent == before
    try:
        d.union_roots(0, 9)
    except IndexError:
        pass
    else:
        assert False


def test_merge_distinct_roots_once():
    d = DisjointSet(4)
    assert d.merge_roots(0, 2) is True
    assert d.find(0) == d.find(2) and d.size[d.find(0)] == 2
    root = d.find(0)
    before = d.parent[:]
    assert d.merge_roots(root, root) is False and d.parent == before
    assert d.find(1) != root
