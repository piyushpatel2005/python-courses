from solution import *

def expect_error(kind, operation):
    try:
        operation()
    except kind:
        return
    raise AssertionError("Expected " + kind.__name__)


def test_minimum_combination():
    'Return the smaller of `left` and `right` in the supplied minimum subclass.'
    for values in [[],[7],[12,5,9],[4,-2,8,3,1]]:
        tree = MinTree(values)
        tree.build()
        for left in range(len(values)+1):
            for right in range(left,len(values)+1):
                assert tree.query(left,right) == min(values[left:right],default=float('inf'))
        if values:
            model=values[:]
            for value in [-99,50]:
                tree.update(0,value)
                model[0]=value
                assert tree.query(0,len(values)) == min(model)
    ordinary=SegmentTree([3,4,8])
    ordinary.build()
    assert ordinary.query(0,3)==15
