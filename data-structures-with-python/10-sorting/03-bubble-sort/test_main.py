from solution import *

def test_01_checkpoint():
    'In `bubble_sort`, run a shrinking pass for each boundary in `pass_stops`.'
    import ast
    import solution
    from pathlib import Path
    tree = ast.parse(Path(solution.__file__).read_text())
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            name = getattr(node.func, "id", getattr(node.func, "attr", ""))
            assert name not in {"sorted", "sort", "heapify", "heappush", "heappop", "nsmallest", "nlargest"}, "Use the taught algorithm rather than a library shortcut."
    a=[7,3,5,1]
    assert bubble_sort(a) is a and a == [1,3,5,7]
    assert bubble_sort([]) == []
    class Record:
        def __init__(self, key, label): self.key, self.label = key, label
        def __lt__(self, other): return self.key < other.key
    first, second = Record(2, 'first'), Record(2, 'second')
    lower = Record(1, 'lower')
    records = [first, second, lower]
    assert bubble_sort(records) is records
    assert records == [lower, first, second]

