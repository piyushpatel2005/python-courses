from solution import *

def test_01_checkpoint():
    "In `rise_once`, repair one parent-child inversion and return the item's resulting index."
    import ast
    import solution
    from pathlib import Path
    tree = ast.parse(Path(solution.__file__).read_text())
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            name = getattr(node.func, "id", getattr(node.func, "attr", ""))
            assert name not in {"sorted", "sort", "heapify", "heappush", "heappop", "nsmallest", "nlargest"}, "Use the taught algorithm rather than a library shortcut."
    a=[3,7,5,9,1]
    assert rise_once(a,4)==1 and a==[3,1,5,9,7]
    assert rise_once(a,0)==0
    assert rise_once([2,2],1)==1

def test_02_checkpoint():
    'In `MinHeap._sift_up`, repair the upward path by repeatedly calling `rise_once`.'
    import ast
    import solution
    from pathlib import Path
    tree = ast.parse(Path(solution.__file__).read_text())
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            name = getattr(node.func, "id", getattr(node.func, "attr", ""))
            assert name not in {"sorted", "sort", "heapify", "heappush", "heappop", "nsmallest", "nlargest"}, "Use the taught algorithm rather than a library shortcut."
    for before in [[3], [3, 7, 5, 9, 1], [1, 4, 2, 7, 5, 1], [2, 2, 2]]:
        h = MinHeap(before)
        data = h.data
        assert h._sift_up(len(before) - 1) is None
        assert h.data is data and is_min_heap(h.data) and sorted(h.data) == sorted(before)
    h = MinHeap([3, 7, 5, 9, 1])
    h._sift_up(4)
    assert h.data == [1, 3, 5, 9, 7]
    source = [1, 2]
    h = MinHeap(source)
    h.data.append(3)
    assert source == [1, 2]

