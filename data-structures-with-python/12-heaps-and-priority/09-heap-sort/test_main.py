from solution import *

def test_01_checkpoint():
    'In `extract_maximum`, move the active maximum to its final slot and repair only the shorter prefix.'
    import ast
    import solution
    from pathlib import Path
    tree = ast.parse(Path(solution.__file__).read_text())
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            name = getattr(node.func, "id", getattr(node.func, "attr", ""))
            assert name not in {"sorted", "sort", "heapify", "heappush", "heappop", "nsmallest", "nlargest"}, "Use the taught algorithm rather than a library shortcut."
    h=MaxHeap([12,7,9,2,4])
    h.data.append(99)
    extract_maximum(h,4)
    assert h.data[4:]==[12,99]
    assert h.data[:4]==[9,7,4,2]
    assert sorted(h.data)==[2,4,7,9,12,99]

def test_02_checkpoint():
    'In `heap_sort`, call the extraction helper for destination indices from the final index down to one.'
    import ast
    import solution
    from pathlib import Path
    tree = ast.parse(Path(solution.__file__).read_text())
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            name = getattr(node.func, "id", getattr(node.func, "attr", ""))
            assert name not in {"sorted", "sort", "heapify", "heappush", "heappop", "nsmallest", "nlargest"}, "Use the taught algorithm rather than a library shortcut."
    for a in ([],[4],[7,2,7,-1,0],list(range(12,0,-1))):
        expected=sorted(a)
        assert heap_sort(a) is a and a==expected

