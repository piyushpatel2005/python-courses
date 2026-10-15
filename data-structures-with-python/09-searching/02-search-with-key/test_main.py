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
    "Return `-1` when no extracted key matches the target."
    calls = []
    def key(record):
        calls.append(record)
        return record[1]
    assert search_with_key([], 9, key) == -1 and calls == []
    records = [("a", 1), ("b", 3)]
    assert search_with_key(records, 9, key) == -1 and calls == records


def test_02_complete_behavior():
    "Return the first matching record index while calling the key function once per visited record."
    _check_technique()
    records = [("a", 7), ("b", 4), ("c", 4)]
    calls = []
    def extract(record):
        calls.append(record)
        return record[1]
    assert search_with_key(records, 4, extract) == 1 and calls == records[:2]
    calls.clear()
    assert search_with_key(records, 8, extract) == -1 and calls == records
    calls.clear()
    assert search_with_key([], 0, extract) == -1 and calls == []
    assert records == [("a", 7), ("b", 4), ("c", 4)]
    def broken(record):
        raise RuntimeError("bad extraction")
    try:
        search_with_key([1], 1, broken)
    except RuntimeError:
        pass
    else:
        assert False, "Do not hide extraction errors"
