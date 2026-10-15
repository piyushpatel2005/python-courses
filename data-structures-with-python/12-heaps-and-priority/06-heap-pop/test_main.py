from solution import *

def test_01_checkpoint():
    'In `MinHeap.pop`, raise `IndexError` before accessing an empty heap.'
    import ast
    import solution
    from pathlib import Path
    tree = ast.parse(Path(solution.__file__).read_text())
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            name = getattr(node.func, "id", getattr(node.func, "attr", ""))
            assert name not in {"sorted", "sort", "heapify", "heappush", "heappop", "nsmallest", "nlargest"}, "Use the taught algorithm rather than a library shortcut."
    h=MinHeap()
    try: h.pop()
    except IndexError: pass
    else: assert False
    assert h.data==[]

def test_02_checkpoint():
    'In `MinHeap.pop`, restore a nonempty remainder by moving the last value to the root and sifting down.'
    import ast
    import solution
    from pathlib import Path
    tree = ast.parse(Path(solution.__file__).read_text())
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            name = getattr(node.func, "id", getattr(node.func, "attr", ""))
            assert name not in {"sorted", "sort", "heapify", "heappush", "heappop", "nsmallest", "nlargest"}, "Use the taught algorithm rather than a library shortcut."
    h=MinHeap([1,3,2,8,6,5])
    data=h.data
    assert h.pop()==1 and h.data is data and is_min_heap(h.data)
    assert sorted(h.data)==[2,3,5,6,8]
    assert [h.pop() for _ in range(5)]==[2,3,5,6,8]
    assert h.data==[]

