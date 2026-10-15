from solution import *

def test_01_checkpoint():
    'In `insertion_sort`, extend the sorted prefix by calling `insert_at` at each next index.'
    import ast
    import solution
    from pathlib import Path
    tree = ast.parse(Path(solution.__file__).read_text())
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            name = getattr(node.func, "id", getattr(node.func, "attr", ""))
            assert name not in {"sorted", "sort", "heapify", "heappush", "heappop", "nsmallest", "nlargest"}, "Use the taught algorithm rather than a library shortcut."
    for original in [[], [8], [5, 1, 5, -1, 0], list(range(12, -1, -1))]:
        a = original[:]
        assert insertion_sort(a) is a and a == sorted(original)
    import solution
    original = solution.insert_at
    calls = []
    def spy(values, index):
        calls.append(index)
        return original(values, index)
    solution.insert_at = spy
    try:
        insertion_sort([4, 3, 2, 1])
    finally:
        solution.insert_at = original
    assert calls == [1, 2, 3]
    class Record:
        def __init__(self, key): self.key = key
        def __lt__(self, other): return self.key < other.key
    first, second, lower = Record(2), Record(2), Record(1)
    records = [first, second, lower]
    assert insertion_sort(records) is records
    assert records == [lower, first, second]

