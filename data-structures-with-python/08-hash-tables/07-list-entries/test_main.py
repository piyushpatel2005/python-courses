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
    "Collect the bucket pairs into a new shallow list in traversal order."
    _check_technique()
    table = HashTable(4)
    assert table.entries() == []
    payload = [1]
    for key, value in [("x", payload), ("a", 2), ("e", 3), ("", None)]: table.put(key, value)
    expected = [pair for bucket in table.buckets for pair in bucket]
    result = table.entries()
    assert result == expected and len(result) == table.size
    result.clear()
    assert table.entries() == expected
    for key, value in table.entries():
        if key == "x": assert value is payload
    assert table.get("x") is payload
