from solution import *

def test_01_checkpoint():
    'In `parent_indices`, return every parent index from the last parent back to the root.'
    import ast
    import solution
    from pathlib import Path
    tree = ast.parse(Path(solution.__file__).read_text())
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            name = getattr(node.func, "id", getattr(node.func, "attr", ""))
            assert name not in {"sorted", "sort", "heapify", "heappush", "heappop", "nsmallest", "nlargest"}, "Use the taught algorithm rather than a library shortcut."
    assert list(parent_indices(8))==[3,2,1,0]
    assert list(parent_indices(7))==[2,1,0]
    assert list(parent_indices(1))==[] and list(parent_indices(0))==[]

def test_02_checkpoint():
    'In `MinHeap.build`, sift down each parent in the descending order supplied by `parent_indices`.'
    import ast
    import solution
    from pathlib import Path
    tree = ast.parse(Path(solution.__file__).read_text())
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            name = getattr(node.func, "id", getattr(node.func, "attr", ""))
            assert name not in {"sorted", "sort", "heapify", "heappush", "heappop", "nsmallest", "nlargest"}, "Use the taught algorithm rather than a library shortcut."
    h = MinHeap([1, 2])
    for values in [[], [4], [9, 3, 8, 1, 6, 2, 2]]:
        before = values[:]
        assert h.build(values) is None
        assert values == before and h.data is not values
        assert is_min_heap(h.data) and sorted(h.data) == sorted(values)
    h = MinHeap()
    original = h._sift_down
    calls = []
    def spy(index):
        calls.append(index)
        original(index)
    h._sift_down = spy
    h.build([9, 8, 7, 6, 5, 4, 3, 2])
    assert calls == [3, 2, 1, 0]
    assert [h.pop() for _ in range(8)] == list(range(2, 10))

