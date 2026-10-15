from solution import *

def _check_technique():
    import ast
    import solution
    with open(solution.__file__, encoding="utf-8") as source_file:
        tree = ast.parse(source_file.read())
    forbidden = ['sorted', 'sort', 'index', 'count', 'bisect', 'bisect_left', 'bisect_right', 'dict', 'set', 'min', 'max', 'insert']
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
    "Complete `shift_right` to add a temporary slot and move the suffix right, copying backward."
    values = [1, 4, 7]
    assert shift_right(values, 1) is None
    assert len(values) == 4 and values[:1] == [1] and values[2:] == [4, 7]
    values = []
    shift_right(values, 0)
    assert values == [0]
    values = [2, 5]
    shift_right(values, 2)
    assert values == [2, 5, 0]


def test_02_complete_behavior():
    "Complete `insert_sorted` to find the upper bound, call the shift helper, write target, and return its position."
    _check_technique()
    from itertools import combinations_with_replacement
    for n in range(6):
        for data in combinations_with_replacement([0, 2, 4], n):
            for target in [-1, 0, 1, 2, 4, 5]:
                values = list(data)
                same = values
                expected_position = sum(x <= target for x in values)
                result = insert_sorted(values, target)
                assert result == expected_position
                assert values is same and values == sorted(list(data) + [target])
    values = [3]
    assert insert_sorted(values, 3) == 1
    assert insert_sorted(values, 3) == 2 and values == [3, 3, 3]
    import solution
    original_bound = solution.upper_bound
    original_shift = solution.shift_right
    calls = []
    def observed_bound(values, target):
        calls.append(("bound", values[:], target))
        return original_bound(values, target)
    def observed_shift(values, position):
        calls.append(("shift", values[:], position))
        return original_shift(values, position)
    solution.upper_bound = observed_bound
    solution.shift_right = observed_shift
    try:
        values = [1, 4, 4, 8]
        assert insert_sorted(values, 4) == 3 and values == [1, 4, 4, 4, 8]
        assert calls == [("bound", [1, 4, 4, 8], 4), ("shift", [1, 4, 4, 8], 3)], "Use upper_bound, then shift_right on the original list"
    finally:
        solution.upper_bound = original_bound
        solution.shift_right = original_shift
