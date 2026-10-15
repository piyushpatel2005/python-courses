from solution import *

def expect_error(kind, operation):
    try:
        operation()
    except kind:
        return
    raise AssertionError("Expected " + kind.__name__)


def test_allocate_new_fenwick():
    'Create a new result tree with one public position per input value.'
    for values in [[], [8], [2,-3,5,7,1]]:
        first,second = Fenwick.from_values(values),Fenwick.from_values(values)
        assert isinstance(first,Fenwick) and first is not second
        assert first.n == len(values) and len(first.tree) == len(values)+1


def test_populate_fenwick():
    'Visit the input positions and add each initial value through `result.add`.'
    source = [2,-3,5,7,1]
    first,second = Fenwick.from_values(source),Fenwick.from_values(source)
    for left in range(6):
        for right in range(left,6):
            assert first.range_sum(left,right) == sum(source[left:right])
    source[0] = 999
    first.add(0,4)
    assert second.range_sum(0,5) == 12
    assert first.range_sum(0,5) == 16
    original = Fenwick.add
    calls = []
    def record(self,position,delta):
        calls.append((position,delta))
        return original(self,position,delta)
    Fenwick.add = record
    try:
        Fenwick.from_values([3,-2,6])
        assert calls == [(0,3),(1,-2),(2,6)]
    finally:
        Fenwick.add = original
