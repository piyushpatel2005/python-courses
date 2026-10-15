from solution import *


def test_compress_both_endpoint_paths():
    d = DisjointSet(6)
    d.parent = [0, 0, 1, 3, 3, 4]
    assert d.compressed_roots(2, 5) == (0, 3)
    assert d.parent[2] == 0 and d.parent[5] == 3


def test_order_roots_by_component_size():
    d = DisjointSet(4)
    d.size = [6, 2, 6, 1]
    assert d.smaller_first(0, 1) == (1, 0)
    assert d.smaller_first(1, 0) == (1, 0)
    assert set(d.smaller_first(0, 2)) == {0, 2}
    assert d.smaller_first(3, 3) == (3, 3)
