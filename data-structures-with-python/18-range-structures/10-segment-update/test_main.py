from solution import *

def expect_error(kind, operation):
    try:
        operation()
    except kind:
        return
    raise AssertionError("Expected " + kind.__name__)


def test_validate_replacement():
    'Reject non-integer arguments or positions outside the real sequence before mutation.'
    tree = SegmentTree([2,4,6])
    tree.build()
    before = tree.tree[:]
    expect_error(IndexError,lambda:tree.update(-1,9))
    expect_error(IndexError,lambda:tree.update(3,9))
    expect_error(TypeError,lambda:tree.update(0,1.5))
    assert tree.tree == before


def test_replace_leaf():
    'Replace the selected leaf with the new value, rather than adding it.'
    tree = SegmentTree([2,4,6])
    tree.build()
    tree.update(1,-8)
    assert tree.tree[tree.size:tree.size+3] == [2,-8,6]
    tree.update(1,5)
    assert tree.tree[tree.size+1] == 5


def test_repair_ancestors():
    'Inside the supplied ancestor loop, recompute the parent from its two children.'
    for values in [[6],[2,-4,8],[3,7,1,9,2]]:
        model = values[:]
        tree,other = SegmentTree(values),SegmentTree(values)
        tree.build()
        other.build()
        for position,value in [(0,-8),(len(values)-1,11),(0,4),(0,4)]:
            tree.update(position,value)
            model[position] = value
            for left in range(len(values)+1):
                for right in range(left,len(values)+1):
                    assert tree.query(left,right) == sum(model[left:right])
        assert other.query(0,len(values)) == sum(values)
