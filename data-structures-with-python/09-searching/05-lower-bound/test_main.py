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
    "Complete `lower_step` to return the next half-open bounds for one nonempty interval."
    values = [3, 8, 8, 8, 12]
    assert lower_step(values, 8, 0, 5) == (0, 2)
    assert lower_step(values, 10, 0, 5) == (3, 5)
    assert lower_step(values, 8, 1, 2) == (1, 1)
    assert lower_step(values, 8, 0, 1) == (1, 1)


def test_02_complete_behavior():
    "Complete `lower_bound` to repeat that step until the bounds meet and return the boundary."
    _check_technique()
    from itertools import combinations_with_replacement
    for n in range(7):
        for data in combinations_with_replacement([-2, 0, 3], n):
            values = list(data)
            for target in [-3, -2, -1, 0, 1, 3, 4]:
                expected = sum(x < target for x in values)
                assert lower_bound(values, target) == expected
            assert values == list(data)
    class AccessBudget:
        def __init__(self, values, budget):
            self.values = values
            self.budget = budget
        def __len__(self):
            return len(self.values)
        def __getitem__(self, index):
            assert isinstance(index, int), "Search with indices, not slices"
            self.budget -= 1
            assert self.budget >= 0, "Halve the interval instead of scanning"
            assert 0 <= index < len(self.values), "Stay inside valid indices"
            return self.values[index]
    values = [5] * 1024
    assert lower_bound(AccessBudget(values, 12), 5) == 0
    assert lower_bound(AccessBudget(values, 12), 6) == 1024
