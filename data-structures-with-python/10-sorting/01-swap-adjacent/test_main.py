from solution import *

def test_01_checkpoint():
    'In `swap_adjacent`, reject an index that does not identify a complete adjacent pair.'
    import ast
    import solution
    from pathlib import Path
    tree = ast.parse(Path(solution.__file__).read_text())
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            name = getattr(node.func, "id", getattr(node.func, "attr", ""))
            assert name not in {"sorted", "sort", "heapify", "heappush", "heappop", "nsmallest", "nlargest"}, "Use the taught algorithm rather than a library shortcut."
    for a, i in (([],0),([2],0),([2,1],-1),([2,1],1)):
        before = a[:]
        try: swap_adjacent(a,i)
        except IndexError: pass
        else: assert False, "Reject an invalid pair"
        assert a == before

def test_02_checkpoint():
    'In `swap_adjacent`, exchange a descending pair and return whether it changed.'
    import ast
    import solution
    from pathlib import Path
    tree = ast.parse(Path(solution.__file__).read_text())
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            name = getattr(node.func, "id", getattr(node.func, "attr", ""))
            assert name not in {"sorted", "sort", "heapify", "heappush", "heappop", "nsmallest", "nlargest"}, "Use the taught algorithm rather than a library shortcut."
    a=[9,3,1]
    assert swap_adjacent(a,0) is True and a == [3,9,1]
    assert swap_adjacent(a,0) is False
    assert swap_adjacent([2,2],0) is False

