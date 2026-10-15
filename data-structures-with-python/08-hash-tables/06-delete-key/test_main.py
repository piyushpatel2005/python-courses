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

def test_01_step():
    "Return `False` when no equal key exists."
    table = HashTable(1)
    table.put("a", 1)
    assert table.delete("missing") is False
    assert table.size == 1 and table.get("a") == 1


def test_02_step():
    "Remove the matching pair and return `True` when it exists."
    table = HashTable(1)
    for key in ["a", "b", "c"]: table.put(key, key)
    assert table.delete("b") is True
    assert table.buckets == [[("a", "a"), ("c", "c")]]
    assert table.delete("b") is False


def test_03_complete_behavior():
    "Decrease size once for each successful removal."
    _check_technique()
    table = HashTable(1)
    for key in ["a", "b", "c", ""]: table.put(key, key)
    for key in ["b", "a", "", "c"]:
        before = table.size
        assert table.delete(key) is True and table.size == before - 1
        assert table.delete(key) is False and table.size == before - 1
        for bucket in table.buckets:
            for remaining, value in bucket: assert table.get(remaining) == value
    assert table.buckets == [[]] and table.size == 0
    table.put("reuse", 9)
    assert table.get("reuse") == 9
    distributed = HashTable(7)
    for key in ["a", "b", "c", "h"]: distributed.put(key, key)
    assert distributed.delete("b") is True and distributed.size == 3
    assert distributed.delete("b") is False
    for key in ["a", "c", "h"]: assert distributed.get(key) == key
    assert all(pair[0] != "b" for bucket in distributed.buckets for pair in bucket)
