from solution import *

def expect_error(kind, operation):
    try:
        operation()
    except kind:
        return
    raise AssertionError("Expected " + kind.__name__)


def test_combine_parent():
    'Inside the supplied reverse loop, set the parent to `_combine` of its two children.'
    for values in [[],[9],[4,-2,7],[8,1,3,-6,2],[2]*8]:
        tree = SegmentTree(values)
        tree.build()
        assert tree.tree[1] == sum(values)
        for i in range(1,tree.size):
            assert tree.tree[i] == tree.tree[2*i]+tree.tree[2*i+1]
        before = tree.tree[:]
        tree.build()
        assert tree.tree == before
