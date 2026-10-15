from solution import *

def test_01_checkpoint():
    'In `minimum_index`, reject an empty or invalid suffix before reading a candidate.'
    import ast
    import solution
    from pathlib import Path
    tree = ast.parse(Path(solution.__file__).read_text())
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            name = getattr(node.func, "id", getattr(node.func, "attr", ""))
            assert name not in {"sorted", "sort", "heapify", "heappush", "heappop", "nsmallest", "nlargest"}, "Use the taught algorithm rather than a library shortcut."
    for a,start in (([],0),([1],-1),([1],1)):
        try: minimum_index(a,start)
        except IndexError: pass
        else: assert False

def test_02_checkpoint():
    'In `minimum_index`, scan the suffix and return the first minimum position without mutation.'
    import ast
    import solution
    from pathlib import Path
    tree = ast.parse(Path(solution.__file__).read_text())
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            name = getattr(node.func, "id", getattr(node.func, "attr", ""))
            assert name not in {"sorted", "sort", "heapify", "heappush", "heappop", "nsmallest", "nlargest"}, "Use the taught algorithm rather than a library shortcut."
    for a,start,expected in (([8,3,3,7],0,1),([0,9,2,2],1,2),([5],0,0)):
        before=a[:]
        assert minimum_index(a,start)==expected and a==before

