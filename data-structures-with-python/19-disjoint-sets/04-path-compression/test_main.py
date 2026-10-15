from solution import *


def test_redirect_preserves_old_link():
    d = DisjointSet(5)
    d.parent = [0, 0, 1, 2, 4]
    before = d.size[:]
    assert d.redirect_parent(3, 0) == 2
    assert d.parent == [0, 0, 1, 0, 4] and d.size == before


def test_compress_entire_path():
    d = DisjointSet(6)
    d.parent = [0, 0, 1, 2, 4, 4]

    def redirect(item, root):
        old = d.parent[item]
        d.parent[item] = root
        return old

    d.redirect_parent = redirect
    d.compress_to(3, 0)
    assert d.parent == [0, 0, 0, 0, 4, 4]
    assert d.size == [1] * 6
    d.compress_to(0, 0)
    assert d.parent == [0, 0, 0, 0, 4, 4]
