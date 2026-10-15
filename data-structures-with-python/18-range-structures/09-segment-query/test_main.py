from solution import *

def expect_error(kind, operation):
    try:
        operation()
    except kind:
        return
    raise AssertionError("Expected " + kind.__name__)


def test_validate_segment_interval():
    'Reject non-integer boundaries or intervals outside the real sequence.'
    tree = SegmentTree([3,4,5])
    tree.build()
    for left,right in [(-1,0),(2,1),(0,4)]:
        expect_error(IndexError,lambda:tree.query(left,right))
    expect_error(TypeError,lambda:tree.query(0.5,2))


def test_consume_left_block():
    'When the left boundary is odd, combine that node into `left_total` and advance left.'
    tree = SegmentTree([2,5,7,11,13,17,19,23])
    tree.build()
    for left,right,expected in [(1,2,5),(3,4,11),(1,4,23)]:
        assert tree.query(left,right) == expected


def test_consume_right_block():
    'When right is odd, decrement the exclusive boundary and combine that node before `right_total`.'
    for values in [[],[7],[4,-3,8],[2,5,-7,1,9],[1]*8]:
        tree = SegmentTree(values)
        tree.build()
        before = tree.tree[:]
        for left in range(len(values)+1):
            for right in range(left,len(values)+1):
                assert tree.query(left,right) == sum(values[left:right])
        assert tree.tree == before
    tree = SegmentTree(list(range(63)))
    tree.build()
    original = tree._combine
    calls = []
    def record(a,b):
        calls.append((a,b))
        return original(a,b)
    tree._combine = record
    assert tree.query(1,62) == sum(range(1,62))
    assert 0 < len(calls) <= 2*tree.size.bit_length()+1
