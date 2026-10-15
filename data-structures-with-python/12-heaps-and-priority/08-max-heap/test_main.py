from solution import *

def test_01_checkpoint():
    'In `larger_child`, choose the larger child strictly inside the active boundary.'
    import ast
    import solution
    from pathlib import Path
    tree = ast.parse(Path(solution.__file__).read_text())
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            name = getattr(node.func, "id", getattr(node.func, "attr", ""))
            assert name not in {"sorted", "sort", "heapify", "heappush", "heappop", "nsmallest", "nlargest"}, "Use the taught algorithm rather than a library shortcut."
    assert larger_child([1,8,6,99],0,3)==1
    assert larger_child([1,6,8,99],0,3)==2
    assert larger_child([1,8,8],0,3)==1
    assert larger_child([1,8,99],0,2)==1
    assert larger_child([1,99],0,1) is None

def test_02_checkpoint():
    'In `MaxHeap._sift_down`, repair the active max-heap prefix by exchanging with its larger child.'
    import ast
    import solution
    from pathlib import Path
    tree = ast.parse(Path(solution.__file__).read_text())
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            name = getattr(node.func, "id", getattr(node.func, "attr", ""))
            assert name not in {"sorted", "sort", "heapify", "heappush", "heappop", "nsmallest", "nlargest"}, "Use the taught algorithm rather than a library shortcut."
    h=MaxHeap([4,-7,0,4,-2,9])
    assert [h.pop() for _ in range(6)]==[9,4,4,0,-2,-7]
    h=MaxHeap()
    h.data=[1,8,6,4,3,99]
    h._sift_down(0,5)
    assert h.data==[8,4,6,1,3,99]
    h=MaxHeap([1,8,6,4,3])
    h.push(10)
    assert h.pop()==10

