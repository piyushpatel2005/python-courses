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
    "Complete `redistribute_entries` to put each stored pair into fresh buckets using its key."
    pairs = [("a", 1), ("b", None), ("", 0)]
    for capacity in [1, 3, 7]:
        result = redistribute_entries(pairs, capacity)
        assert len(result) == capacity
        assert len({id(bucket) for bucket in result}) == capacity
        assert sorted(pair for bucket in result for pair in bucket) == sorted(pairs)
        for key, value in pairs: assert (key, value) in result[bucket_index(key, capacity)]
    assert pairs == [("a", 1), ("b", None), ("", 0)]


def test_02_complete_behavior():
    "Complete `rehash` to validate first, snapshot the pairs, and replace the bucket collection with the helper result."
    _check_technique()
    table = HashTable(1)
    payload = []
    expected = [("a", 1), ("b", None), ("", 0), ("object", payload), ("café", 8)]
    for key, value in expected: table.put(key, value)
    for capacity in [7, 2, 2, 1, 13]:
        old = table.buckets
        assert table.rehash(capacity) is None
        assert table.buckets is not old and len(table.buckets) == capacity
        assert table.size == len(expected)
        for key, value in expected:
            assert table.get(key) is value
            assert (key, value) in table.buckets[bucket_index(key, capacity)]
        assert len({id(bucket) for bucket in table.buckets}) == capacity
    saved = table.buckets
    for bad in [0, -1, True, 2.5]:
        try:
            table.rehash(bad)
        except ValueError:
            pass
        else:
            assert False, "Reject invalid capacity"
        assert table.buckets is saved and table.size == len(expected)
    empty = HashTable(3)
    empty.rehash(1)
    assert empty.entries() == [] and empty.size == 0
