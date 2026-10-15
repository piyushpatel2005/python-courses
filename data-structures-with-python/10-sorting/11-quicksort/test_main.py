from solution import *

def test_01_checkpoint():
    'In `split_three`, separate a nonempty input into less, equal, and greater groups without mutation.'
    import ast
    import solution
    from pathlib import Path
    tree = ast.parse(Path(solution.__file__).read_text())
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            name = getattr(node.func, "id", getattr(node.func, "attr", ""))
            assert name not in {"sorted", "sort", "heapify", "heappush", "heappop", "nsmallest", "nlargest"}, "Use the taught algorithm rather than a library shortcut."
    a=[7,2,4,1,4]
    assert split_three(a)==([2,1],[4,4],[7]) and a==[7,2,4,1,4]
    assert split_three([3,3,3])==([],[3,3,3],[])

def test_02_checkpoint():
    'In `quicksort`, return a fresh copy for the recursive base case.'
    import ast
    import solution
    from pathlib import Path
    tree = ast.parse(Path(solution.__file__).read_text())
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            name = getattr(node.func, "id", getattr(node.func, "attr", ""))
            assert name not in {"sorted", "sort", "heapify", "heappush", "heappop", "nsmallest", "nlargest"}, "Use the taught algorithm rather than a library shortcut."
    for a in ([],[3]):
        result=quicksort(a)
        assert result==a and result is not a

def test_03_checkpoint():
    'In `quicksort`, recursively sort the smaller and greater groups, then concatenate around the equal group.'
    import ast
    import solution
    from pathlib import Path
    tree = ast.parse(Path(solution.__file__).read_text())
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            name = getattr(node.func, "id", getattr(node.func, "attr", ""))
            assert name not in {"sorted", "sort", "heapify", "heappush", "heappop", "nsmallest", "nlargest"}, "Use the taught algorithm rather than a library shortcut."
    for a in ([5,2,5,-1,5],[9,8,7,6],list(range(12))):
        before=a[:]
        result=quicksort(a)
        assert result==sorted(before) and a==before and result is not a

