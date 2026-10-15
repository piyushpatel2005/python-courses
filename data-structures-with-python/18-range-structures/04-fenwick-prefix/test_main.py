from solution import *

def expect_error(kind, operation):
    try:
        operation()
    except kind:
        return
    raise AssertionError("Expected " + kind.__name__)


def test_validate_prefix_boundary():
    'Reject non-integer or out-of-range `end` boundaries; zero and n are allowed.'
    tree = Fenwick(3)
    expect_error(IndexError, lambda: tree.prefix(-1))
    expect_error(IndexError, lambda: tree.prefix(4))
    expect_error(TypeError, lambda: tree.prefix(1.5))


def test_accumulate_prefix_blocks():
    'Inside the supplied decreasing lowbit loop, add the current block to `total`.'
    for values in [[], [6], [3,-4,7,2,9], [2]*11]:
        tree = Fenwick(len(values))
        for position,value in enumerate(values):
            tree.add(position,value)
        before = tree.tree[:]
        for end in range(len(values)+1):
            assert tree.prefix(end) == sum(values[:end])
        assert tree.tree == before
        if values:
            tree.add(0,-8)
            assert tree.prefix(len(values)) == sum(values)-8
