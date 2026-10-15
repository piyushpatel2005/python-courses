from solution import *

def test_01_checkpoint():
    'In `retain_candidate`, keep one incoming candidate only when capacity or its value justifies admission.'
    h=[]
    retain_candidate(h,5,3)
    retain_candidate(h,2,3)
    retain_candidate(h,7,3)
    assert sorted(h)==[2,5,7]
    retain_candidate(h,1,3)
    assert sorted(h)==[2,5,7]
    retain_candidate(h,6,3)
    assert sorted(h)==[5,6,7]
    retain_candidate(h,5,3)
    assert len(h)==3 and sorted(h)==[5,6,7]

def test_02_checkpoint():
    'In `top_k`, reject negative k and return immediately for zero without consuming input.'
    def forbidden():
        raise AssertionError("Do not consume this input")
        yield 1
    assert top_k(forbidden(),0)==[]
    try: top_k(forbidden(),-1)
    except ValueError: pass
    else: assert False

def test_03_checkpoint():
    'In `top_k`, drain and reverse the retained heap to return descending results.'
    for values, k in [([], 3), ([4], 3), ([5, 2, 5, -1, 7], 3), ([3, 1, 2], 1), ([2, 2, 2], 2)]:
        assert top_k(iter(values), k) == sorted(values, reverse=True)[:k]
    def forbidden_stream():
        raise AssertionError('Do not consume input for k=0 or negative k')
        yield 1
    assert top_k(forbidden_stream(), 0) == []
    try:
        top_k(forbidden_stream(), -1)
        assert False
    except ValueError:
        pass
    import solution
    original = solution.heapq.heappush
    sizes = []
    def spy(heap, value):
        result = original(heap, value)
        sizes.append(len(heap))
        return result
    solution.heapq.heappush = spy
    try:
        assert top_k(iter(range(30)), 4) == [29, 28, 27, 26]
    finally:
        solution.heapq.heappush = original
    assert sizes and max(sizes) <= 4

