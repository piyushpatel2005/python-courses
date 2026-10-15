from solution import *

def test_01_checkpoint():
    'In `shift_larger`, shift larger predecessors right and return the final gap index.'
    import ast
    import solution
    from pathlib import Path
    tree = ast.parse(Path(solution.__file__).read_text())
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            name = getattr(node.func, "id", getattr(node.func, "attr", ""))
            assert name not in {"sorted", "sort", "heapify", "heappush", "heappop", "nsmallest", "nlargest"}, "Use the taught algorithm rather than a library shortcut."
    a=[2,6,9,4,0]
    assert shift_larger(a,3,4)==1 and a==[2,6,6,9,0]
    assert shift_larger([2,2],1,2)==1
    assert shift_larger([3],0,3)==0

def test_02_checkpoint():
    'In `insert_at`, reject an invalid insertion position before mutation.'
    import ast
    import solution
    from pathlib import Path
    tree = ast.parse(Path(solution.__file__).read_text())
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            name = getattr(node.func, "id", getattr(node.func, "attr", ""))
            assert name not in {"sorted", "sort", "heapify", "heappush", "heappop", "nsmallest", "nlargest"}, "Use the taught algorithm rather than a library shortcut."
    for a,i in (([],0),([1],-1),([1],1)):
        try: insert_at(a,i)
        except IndexError: pass
        else: assert False

def test_03_checkpoint():
    'In `insert_at`, fill the returned gap with the saved item and return the same list.'
    import ast
    import solution
    from pathlib import Path
    tree = ast.parse(Path(solution.__file__).read_text())
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            name = getattr(node.func, "id", getattr(node.func, "attr", ""))
            assert name not in {"sorted", "sort", "heapify", "heappush", "heappop", "nsmallest", "nlargest"}, "Use the taught algorithm rather than a library shortcut."
    a=[2,6,9,4,0]
    assert insert_at(a,3) is a and a == [2,4,6,9,0]
    assert insert_at([4],0)==[4]
    assert insert_at([1,2,2],2)==[1,2,2]

