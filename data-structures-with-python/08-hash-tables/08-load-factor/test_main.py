from solution import *

def _check_technique():
    import ast
    import solution
    with open(solution.__file__, encoding="utf-8") as source_file:
        tree = ast.parse(source_file.read())
    forbidden = ['dict', 'set', 'Counter', 'defaultdict']
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

def test_01_complete_behavior():
    "Return `size / len(buckets)` from `load_factor`."
    _check_technique()
    table = HashTable(4)
    assert table.load_factor() == 0.0
    for i, key in enumerate(["a", "b", "c", "d", "e"]):
        table.put(key, i)
        assert table.load_factor() == (i + 1) / 4
    assert isinstance(table.load_factor(), float)
    table.put("a", 99)
    assert table.load_factor() == 1.25
    table.delete("c")
    assert table.load_factor() == 1.0 and table.size == 4
