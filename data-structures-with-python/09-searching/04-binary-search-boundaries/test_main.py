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
    "Complete `validate_bounds` with the half-open integer-bound rules."
    for lo, hi in [(-1, 2), (2, 1), (0, 4), (True, 2), (0, 2.0)]:
        try: validate_bounds([1, 2, 3], lo, hi)
        except ValueError: pass
        else: assert False, "Reject invalid bounds"
    assert validate_bounds([1, 2, 3], 3, 3) is None


def test_02_step():
    "Return `-1` for a valid empty search interval."
    assert binary_search_range([1, 2, 3], 2, 1, 1) == -1
    assert binary_search_range([], 2, 0, 0) == -1


def test_03_complete_behavior():
    "Replace the loop pause with a binary search confined to the supplied bounds."
    _check_technique()
    values = [1, 3, 3, 6, 9]
    for lo in range(len(values)+1):
        for hi in range(lo, len(values)+1):
            for target in [0, 1, 3, 4, 6, 9, 10]:
                result = binary_search_range(values, target, lo, hi)
                assert (result == -1) if target not in values[lo:hi] else (lo <= result < hi and values[result] == target)
    for lo, hi in [(-1, 3), (2, 1), (0, 6), (True, 3), (0, 2.0)]:
        try:
            binary_search_range(values, 3, lo, hi)
        except ValueError:
            pass
        else:
            assert False, "Reject invalid bounds"
    class Region:
        def __len__(self): return 8
        def __getitem__(self, index):
            assert 2 <= index < 6, "Do not read outside the requested range"
            return index * 2
    assert binary_search_range(Region(), 8, 2, 6) == 4
    assert binary_search_range(Region(), 1, 2, 6) == -1
    class BoundedRegion:
        reads = 0
        def __len__(self): return 2048
        def __getitem__(self, index):
            assert isinstance(index, int) and 256 <= index < 1792
            self.reads += 1
            assert self.reads <= 26, "Halve the region instead of scanning it"
            return index * 2
    assert binary_search_range(BoundedRegion(), 3000, 256, 1792) == 1500
    assert binary_search_range(BoundedRegion(), 3001, 256, 1792) == -1
