from solution import *

def expect_error(kind, operation):
    try:
        operation()
    except kind:
        return
    raise AssertionError("Expected " + kind.__name__)


def test_segment_real_length():
    'Record the real input length in `n`.'
    for values in [[],[4],[2,8,3]]:
        assert SegmentTree(values).n == len(values)


def test_segment_capacity():
    'Double `size` from one until it can hold all real values.'
    for values,capacity in [([],1),([4],1),([2,8,3],4),([1]*5,8),([1]*8,8)]:
        assert SegmentTree(values).size == capacity


def test_segment_storage():
    'Allocate a fresh `tree` list with `2 * size` identity entries.'
    first,second = SegmentTree([2,8,3]),SegmentTree([2,8,3])
    assert len(first.tree) == 2*first.size
    assert first.tree[:first.size] == [0]*first.size
    assert first.tree[first.size+first.n:] == [0]*(first.size-first.n)
    first.tree[0] = 99
    assert second.tree[0] == 0


def test_segment_real_leaves():
    'Copy each input value into its real leaf at `size + position`.'
    for source in [[4],[2,8,3],[5,-1,7,2,6]]:
        original = source[:]
        tree = SegmentTree(source)
        assert tree.tree[tree.size:tree.size+tree.n] == original
        source[0] = 999
        assert tree.tree[tree.size] == original[0]
