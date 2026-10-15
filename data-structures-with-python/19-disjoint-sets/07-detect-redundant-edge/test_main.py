from solution import *


def test_redundancy_updates_connectivity():
    d = DisjointSet(4)
    assert edge_is_redundant(d, 0, 1) is False
    assert edge_is_redundant(d, 1, 2) is False
    assert edge_is_redundant(d, 2, 0) is True
    assert edge_is_redundant(d, 3, 3) is True


def test_edge_result_preserves_orientation():
    assert edge_pair(4, 1) == (4, 1)
    assert edge_pair(0, 0) == (0, 0)
    assert type(edge_pair(2, 3)) is tuple
