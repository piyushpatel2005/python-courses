from solution import *

def test_01_checkpoint():
    'In `scan_partition`, scan non-pivot items into the smaller region and return its boundary.'
    import ast
    import solution
    from pathlib import Path
    tree = ast.parse(Path(solution.__file__).read_text())
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            name = getattr(node.func, "id", getattr(node.func, "attr", ""))
            assert name not in {"sorted", "sort", "heapify", "heappush", "heappop", "nsmallest", "nlargest"}, "Use the taught algorithm rather than a library shortcut."
    a=[99,7,2,6,4,88]
    p=scan_partition(a,1,4)
    assert p==2 and a[4]==4 and a[0]==99 and a[-1]==88
    assert all(x<4 for x in a[1:p])
    assert all(x>=4 for x in a[p:4])
    assert scan_partition([2,2,2],0,2)==0

def test_02_checkpoint():
    'In `partition`, reject an invalid inclusive interval before mutation.'
    import ast
    import solution
    from pathlib import Path
    tree = ast.parse(Path(solution.__file__).read_text())
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            name = getattr(node.func, "id", getattr(node.func, "attr", ""))
            assert name not in {"sorted", "sort", "heapify", "heappush", "heappop", "nsmallest", "nlargest"}, "Use the taught algorithm rather than a library shortcut."
    for lo,hi in ((-1,1),(0,2),(1,0)):
        a=[2,1]
        try: partition(a,lo,hi)
        except IndexError: pass
        else: assert False
        assert a==[2,1]

def test_03_checkpoint():
    'In `partition`, exchange the pivot into the returned boundary and return that index.'
    import ast
    import solution
    from pathlib import Path
    tree = ast.parse(Path(solution.__file__).read_text())
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            name = getattr(node.func, "id", getattr(node.func, "attr", ""))
            assert name not in {"sorted", "sort", "heapify", "heappush", "heappop", "nsmallest", "nlargest"}, "Use the taught algorithm rather than a library shortcut."
    for a, low, high in [([99, 7, 2, 6, 4, -99], 1, 4), ([2, 2, 2], 0, 2), ([3], 0, 0), ([4, 1, 3, 2], 0, 3)]:
        before = a[:]
        pivot = a[high]
        p = partition(a, low, high)
        assert low <= p <= high and a[p] == pivot
        assert all(x < pivot for x in a[low:p])
        assert all(not x < pivot for x in a[p+1:high+1])
        assert sorted(a[low:high+1]) == sorted(before[low:high+1])
        assert a[:low] == before[:low] and a[high+1:] == before[high+1:]
    a = [7, 2, 6, 4]
    assert partition(a, 0, 3) == 1 and a == [2, 4, 6, 7]
    for low, high in [(-1, 1), (0, 2), (1, 0)]:
        a = [2, 1]
        try:
            partition(a, low, high)
            assert False
        except IndexError:
            pass
        assert a == [2, 1]

