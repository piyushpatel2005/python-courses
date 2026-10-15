from solution import *

def expect_error(kind, operation):
    try:
        operation()
    except kind:
        return
    raise AssertionError("Expected " + kind.__name__)


def test_validate_interval():
    'Reject non-integer boundaries and intervals outside `0 <= left <= right <= n`.'
    tree = Fenwick(4)
    for left,right in [(-1,0),(2,1),(0,5)]:
        expect_error(IndexError, lambda: tree.range_sum(left,right))
    expect_error(TypeError, lambda: tree.range_sum(0.5,2))


def test_subtract_prefixes():
    'Return the right prefix minus the left prefix.'
    for values in [[], [-5], [4,-7,3,9,1]]:
        tree = Fenwick(len(values))
        for position,value in enumerate(values):
            tree.add(position,value)
        for left in range(len(values)+1):
            for right in range(left,len(values)+1):
                assert tree.range_sum(left,right) == sum(values[left:right])
        if values:
            tree.add(len(values)-1,6)
            assert tree.range_sum(len(values)-1,len(values)) == values[-1]+6
