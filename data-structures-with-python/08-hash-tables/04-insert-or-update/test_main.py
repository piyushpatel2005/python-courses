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
    "Append a pair and increase size when its key is not already in the bucket."
    table = HashTable(7)
    for i, key in enumerate(["a", "b", "h"]):
        assert table.put(key, i) is None
        assert (key, i) in table.buckets[bucket_index(key, 7)]
        assert table.size == i + 1


def test_02_complete_behavior():
    "Replace the value of an equal key without adding a pair or changing size."
    _check_technique()
    table = HashTable(1)
    for key, value in [("a", 1), ("b", 2), ("a", None), ("", 0), ("b", 9)]:
        assert table.put(key, value) is None
    assert table.size == 3
    assert sorted(table.buckets[0]) == [("", 0), ("a", None), ("b", 9)]
    payload = []
    table.put("object", payload)
    assert table.buckets[0][-1][1] is payload
    other = HashTable(1)
    assert other.size == 0 and other.buckets == [[]]
    distributed = HashTable(7)
    for key in ["a", "b", "c", "h"]:
        distributed.put(key, key)
        assert (key, key) in distributed.buckets[bucket_index(key, 7)]
    distributed.put("b", 10)
    assert distributed.size == 4
    assert ("b", 10) in distributed.buckets[bucket_index("b", 7)]
