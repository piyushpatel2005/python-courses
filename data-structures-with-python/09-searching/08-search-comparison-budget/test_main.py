from solution import *

def _check_technique():
    import ast
    import solution
    with open(solution.__file__, encoding="utf-8") as source_file:
        tree = ast.parse(source_file.read())
    forbidden = ['sorted', 'sort', 'index', 'count', 'bisect', 'bisect_left', 'bisect_right', 'dict', 'set', 'min', 'max']
    for top in tree.body:
        if not isinstance(top, (ast.FunctionDef, ast.ClassDef, ast.Import, ast.ImportFrom)):
            continue
        for node in ast.walk(top):
            if isinstance(node, ast.Call):
                name = node.func.id if isinstance(node.func, ast.Name) else getattr(node.func, "attr", "")
                assert name not in forbidden, "Implement the stated algorithm rather than a shortcut"
            if isinstance(node, (ast.Import, ast.ImportFrom)):
                names = [alias.name for alias in node.names] + [getattr(node, "module", "") or ""]
                assert not any(name.split(".")[0] in forbidden for name in names), "Use the taught algorithm"
            if "dict" in forbidden:
                assert not isinstance(node, (ast.Dict, ast.DictComp, ast.Set, ast.SetComp)), "Use the bucket representation"

def test_01_step():
    "Complete `compare_at` to call the comparator once for the requested item and return its relation."
    calls = []
    def compare(a, b):
        calls.append((a, b))
        return -7 if a < b else 9 if a > b else 0
    assert compare_at([3, 8, 12], 1, 10, compare) == -7
    assert calls == [(8, 10)]
    assert compare_at([3, 8, 12], 2, 10, compare) == 9
    assert len(calls) == 2


def test_02_complete_behavior():
    "Complete `measured_binary_search` to halve the interval and count the actual calls to that helper."
    _check_technique()
    for n in [0, 1, 2, 3, 7, 16, 63, 128]:
        values = list(range(0, n * 2, 2))
        for target in range(-1, n * 2 + 1):
            calls = []
            def compare(a, b):
                calls.append((a, b))
                assert len(calls) <= n.bit_length(), "Use halving, not a scan or repeated comparisons"
                return (a > b) - (a < b)
            index, probes = measured_binary_search(values, target, compare)
            assert probes == len(calls) and probes <= n.bit_length()
            assert (index == -1) if target not in values else (0 <= index < n and values[index] == target)
    assert measured_binary_search([], 1) == (-1, 0)
    assert measured_binary_search([1, 4, 9, 13, 18], 9) == (2, 1)
    def descending(a, b): return (a < b) - (a > b)
    assert measured_binary_search([9, 6, 2], 6, descending) == (1, 1)
    assert measured_binary_search([5, 5, 5], 5)[0] in range(3)
