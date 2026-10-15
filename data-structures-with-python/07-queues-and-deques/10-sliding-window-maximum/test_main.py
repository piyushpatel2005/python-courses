from solution import *

def _check_technique():
    import ast
    import solution
    with open(solution.__file__, encoding="utf-8") as source_file:
        tree = ast.parse(source_file.read())
    forbidden = ['max', 'sorted', 'sort']
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
    "Complete `validate_window` with the width and empty-input rules."
    for values, k in [([], 1), ([2], 0), ([2], 2), ([2], True), ([2], 1.0)]:
        try: validate_window(values, k)
        except ValueError: pass
        else: assert False, "Reject invalid width"
    assert validate_window([2, 4], 2) is None


def test_02_step():
    "Complete `advance_candidates` to expire old indices, discard dominated rear candidates, and append the current index."
    from collections import deque
    for values in [[8, 6, 4, 2, 9], [1, 5, 5, 2, 7]]:
        candidates = deque()
        for i in range(len(values)):
            advance_candidates(values, candidates, i, 3)
            indices = list(candidates)
            assert indices and indices[-1] == i
            assert all(max(0, i - 2) <= j <= i for j in indices)
            assert all(a < b for a, b in zip(indices, indices[1:]))
            assert all(values[a] >= values[b] for a, b in zip(indices, indices[1:]))
            assert values[indices[0]] == max(values[max(0, i-2):i+1])


def test_03_complete_behavior():
    "Complete `window_maxima` to call both helpers and collect the front value after each full window."
    _check_technique()
    from itertools import product
    for n in range(1, 6):
        for values in product([-2, 0, 3], repeat=n):
            values = list(values)
            saved = values[:]
            for k in range(1, n + 1):
                expected = [max(values[i:i+k]) for i in range(n-k+1)]
                assert window_maxima(values, k) == expected
            assert values == saved
    for values, k in [([], 1), ([1], 0), ([1], 2), ([1], True), ([1], 1.0)]:
        try:
            window_maxima(values, k)
        except ValueError:
            pass
        else:
            assert False, "Reject invalid widths"
    class Counted(list):
        reads = 0
        def __getitem__(self, index):
            assert not isinstance(index, slice), "Do not rescan window slices"
            self.reads += 1
            return super().__getitem__(index)
    values = Counted(list(range(128, 0, -1)))
    assert window_maxima(values, 64) == list(range(128, 63, -1))
    assert values.reads <= 8 * len(values), "Maintain candidates rather than rescanning windows"
