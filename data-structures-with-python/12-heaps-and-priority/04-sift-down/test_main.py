from solution import *

def test_01_checkpoint():
    'In `smaller_child`, choose the smaller existing child, favoring the left on a tie.'
    import ast
    import solution
    from pathlib import Path
    tree = ast.parse(Path(solution.__file__).read_text())
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            name = getattr(node.func, "id", getattr(node.func, "attr", ""))
            assert name not in {"sorted", "sort", "heapify", "heappush", "heappop", "nsmallest", "nlargest"}, "Use the taught algorithm rather than a library shortcut."
    assert smaller_child([9,3,5],0)==1
    assert smaller_child([9,5,3],0)==2
    assert smaller_child([9,2,2],0)==1
    assert smaller_child([9,3],0)==1
    assert smaller_child([9],0) is None

def test_02_checkpoint():
    'In `MinHeap._sift_down`, move down through smaller children until the subtree obeys heap order.'
    import ast
    import solution
    from pathlib import Path
    tree = ast.parse(Path(solution.__file__).read_text())
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            name = getattr(node.func, "id", getattr(node.func, "attr", ""))
            assert name not in {"sorted", "sort", "heapify", "heappush", "heappop", "nsmallest", "nlargest"}, "Use the taught algorithm rather than a library shortcut."
    for before in [[9, 3, 5, 7, 8, 6], [5, 2], [2], [2, 2, 2], [8, 4, 1, 7, 6, 2, 3]]:
        h = MinHeap(before)
        data = h.data
        assert h._sift_down(0) is None
        assert h.data is data and is_min_heap(h.data) and sorted(h.data) == sorted(before)
    h = MinHeap([0, 9, 2, 3, 4])
    h._sift_down(1)
    assert h.data == [0, 3, 2, 9, 4]
    h = MinHeap([7, 2, 2])
    h._sift_down(0)
    assert h.data == [2, 7, 2]

