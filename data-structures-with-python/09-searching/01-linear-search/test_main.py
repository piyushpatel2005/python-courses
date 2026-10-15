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
    "Return `-1` after the scan finishes without a match."
    assert linear_search([], 4) == -1
    assert linear_search([1, 3, 5], 4) == -1


def test_02_complete_behavior():
    "Return the first equal item's index from inside the scan."
    _check_technique()
    from itertools import product
    for n in range(5):
        for source in product([0, 1, 2], repeat=n):
            values = list(source)
            for target in [-1, 0, 1, 2, 3]:
                expected = next((i for i, x in enumerate(values) if x == target), -1)
                assert linear_search(values, target) == expected
            assert values == list(source)
    assert linear_search([None, "x", None], None) == 0
