from solution import *

def test_01_checkpoint():
    'In `selection_sort`, place each remaining suffix minimum into the next destination.'
    import ast
    import solution
    from pathlib import Path
    tree = ast.parse(Path(solution.__file__).read_text())
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            name = getattr(node.func, "id", getattr(node.func, "attr", ""))
            assert name not in {"sorted", "sort", "heapify", "heappush", "heappop", "nsmallest", "nlargest"}, "Use the taught algorithm rather than a library shortcut."
    for original in [[], [5], [3, -1, 3, 2], [8, 7, 6, 5, 4]]:
        a = original[:]
        assert selection_sort(a) is a and a == sorted(original)
    import solution
    original = solution.minimum_index
    calls = []
    def spy(values, start):
        calls.append(start)
        return original(values, start)
    solution.minimum_index = spy
    try:
        selection_sort([4, 1, 3, 2])
    finally:
        solution.minimum_index = original
    assert calls == [0, 1, 2]

