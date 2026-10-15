from solution import *

def test_01_checkpoint():
    'In `bubble_pass`, reject an exclusive stop outside the list boundaries.'
    import ast
    import solution
    from pathlib import Path
    tree = ast.parse(Path(solution.__file__).read_text())
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            name = getattr(node.func, "id", getattr(node.func, "attr", ""))
            assert name not in {"sorted", "sort", "heapify", "heappush", "heappop", "nsmallest", "nlargest"}, "Use the taught algorithm rather than a library shortcut."
    for stop in (-1, 4):
        a=[2,1]
        try: bubble_pass(a,stop)
        except ValueError: pass
        else: assert False
        assert a == [2,1]

def test_02_checkpoint():
    'In `bubble_pass`, scan every active pair and return whether any exchange occurred.'
    import ast
    import solution
    from pathlib import Path
    tree = ast.parse(Path(solution.__file__).read_text())
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            name = getattr(node.func, "id", getattr(node.func, "attr", ""))
            assert name not in {"sorted", "sort", "heapify", "heappush", "heappop", "nsmallest", "nlargest"}, "Use the taught algorithm rather than a library shortcut."
    a=[8,3,6,2,-4]
    assert bubble_pass(a,4) is True and a == [3,6,2,8,-4]
    assert bubble_pass([3,1,9],3) is True
    for a in ([],[2],[1,1,2]): assert bubble_pass(a,len(a)) is False

