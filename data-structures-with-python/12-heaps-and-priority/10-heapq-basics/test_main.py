from solution import *

def test_01_checkpoint():
    'In `make_heap`, copy the input, heapify the copy, and return the owned heap list.'
    a=[8,2,7,1]
    h=make_heap(a)
    assert h is not a and a==[8,2,7,1]
    assert sorted(h)==sorted(a)
    assert all(h[(i-1)//2]<=h[i] for i in range(1,len(h)))
    assert make_heap([])==[]

def test_02_checkpoint():
    'In `heapq_order`, drain the copied heap with `heapq.heappop` into a new ordered result.'
    for values in [[], [4], [8, 2, 8, -1, 3]]:
        before = values[:]
        result = heapq_order(values)
        assert result == sorted(values) and values == before and result is not values
    import solution
    original_heapify, original_pop = solution.heapq.heapify, solution.heapq.heappop
    calls = []
    def heapify_spy(values):
        calls.append('heapify')
        return original_heapify(values)
    def pop_spy(values):
        calls.append('pop')
        return original_pop(values)
    solution.heapq.heapify, solution.heapq.heappop = heapify_spy, pop_spy
    try:
        heapq_order([4, 1, 2])
    finally:
        solution.heapq.heapify, solution.heapq.heappop = original_heapify, original_pop
    assert calls == ['heapify', 'pop', 'pop', 'pop']

