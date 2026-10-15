from solution import *

def expect_error(kind, operation):
    try:
        operation()
    except kind:
        return
    raise AssertionError("Expected " + kind.__name__)


def test_validate_size():
    'Validate the requested size with the nonnegative-integer helper.'
    expect_error(ValueError, lambda: Fenwick(-1))
    expect_error(TypeError, lambda: Fenwick(1.5))


def test_store_length():
    'Set `n` to the requested public size.'
    for size in [0, 1, 5]:
        assert Fenwick(size).n == size


def test_allocate_cells():
    'Allocate a fresh zero-filled list of `size + 1` cells for `tree`.'
    for size in [0, 1, 5, 8]:
        first, second = Fenwick(size), Fenwick(size)
        assert first.tree == [0]*(size+1)
        first.tree[0] = 9
        assert second.tree == [0]*(size+1)
