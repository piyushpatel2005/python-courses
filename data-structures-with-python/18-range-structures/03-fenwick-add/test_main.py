from solution import *

def expect_error(kind, operation):
    try:
        operation()
    except kind:
        return
    raise AssertionError("Expected " + kind.__name__)


def test_validate_add_arguments():
    'Reject invalid types or a public position outside `0 <= position < n` before mutation.'
    tree = Fenwick(3)
    before = tree.tree[:]
    expect_error(IndexError, lambda: tree.add(-1, 4))
    expect_error(IndexError, lambda: tree.add(3, 4))
    expect_error(TypeError, lambda: tree.add(0, 1.5))
    expect_error(IndexError, lambda: Fenwick(0).add(0, 1))
    assert tree.tree == before


def test_propagate_delta():
    'Inside the supplied lowbit loop, add `delta` to the current internal cell.'
    for size in [1, 3, 5, 8]:
        tree, other = Fenwick(size), Fenwick(size)
        model = [0]*size
        for position, delta in [(0,4), (size-1,-2), (size//2,7), (0,-1)]:
            tree.add(position, delta)
            model[position] += delta
            assert tree.tree[0] == 0
            for i in range(1,size+1):
                assert tree.tree[i] == sum(model[i-(i & -i):i])
        assert other.tree == [0]*(size+1)
