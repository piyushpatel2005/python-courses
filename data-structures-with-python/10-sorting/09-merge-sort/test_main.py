from solution import *

def test_01_checkpoint():
    'In `merge_sort`, return a fresh copy for inputs with fewer than two items.'
    import ast
    import solution
    from pathlib import Path
    tree = ast.parse(Path(solution.__file__).read_text())
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            name = getattr(node.func, "id", getattr(node.func, "attr", ""))
            assert name not in {"sorted", "sort", "heapify", "heappush", "heappop", "nsmallest", "nlargest"}, "Use the taught algorithm rather than a library shortcut."
    for a in ([],[4]):
        result=merge_sort(a)
        assert result==a and result is not a

def test_02_checkpoint():
    'In `merge_sort`, recursively sort both halves and combine them with `merge_runs`.'
    import ast
    import solution
    from pathlib import Path
    tree = ast.parse(Path(solution.__file__).read_text())
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            name = getattr(node.func, "id", getattr(node.func, "attr", ""))
            assert name not in {"sorted", "sort", "heapify", "heappush", "heappop", "nsmallest", "nlargest"}, "Use the taught algorithm rather than a library shortcut."
    for a in ([9,2],[5,2,5,-1],[8,7,6,5,4]):
        before=a[:]
        assert merge_sort(a)==sorted(before) and a==before
    class Record:
        def __init__(self, key): self.key = key
        def __lt__(self, other): return self.key < other.key
    first, second, lower = Record(2), Record(2), Record(1)
    records = [first, lower, second]
    result = merge_sort(records)
    assert result == [lower, first, second]
    assert records == [first, lower, second] and result is not records

