from solution import *

def test_01_checkpoint():
    'In `MinHeap.push`, append the new leaf and pass its index to the completed sift-up helper.'
    import ast
    import solution
    from pathlib import Path
    tree = ast.parse(Path(solution.__file__).read_text())
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            name = getattr(node.func, "id", getattr(node.func, "attr", ""))
            assert name not in {"sorted", "sort", "heapify", "heappush", "heappop", "nsmallest", "nlargest"}, "Use the taught algorithm rather than a library shortcut."
    h = MinHeap()
    seen = []
    for value in [7, -1, 3, 3, 0, 9]:
        seen.append(value)
        assert h.push(value) is None
        assert is_min_heap(h.data) and sorted(h.data) == sorted(seen)
    other = MinHeap()
    other.push(99)
    assert 99 not in h.data
    h = MinHeap([1, 3])
    calls = []
    original = h._sift_up
    def spy(index):
        calls.append((index, h.data[index]))
        original(index)
    h._sift_up = spy
    h.push(0)
    assert calls == [(2, 0)] and h.data[0] == 0

