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
    "Allocate independent empty buckets in `HashTable.__init__` after the supplied capacity check."
    a, b = HashTable(3), HashTable(3)
    assert a.buckets == [[], [], []]
    a.buckets[0].append(("x", 1))
    assert a.buckets[1:] == [[], []] and b.buckets == [[], [], []]


def test_02_complete_behavior():
    "Initialize the distinct-key count `size` to zero."
    _check_technique()
    for capacity in [1, 4, 8]:
        a, b = HashTable(capacity), HashTable(capacity)
        assert a.buckets == [[] for _ in range(capacity)] and a.size == 0
        assert len({id(bucket) for bucket in a.buckets}) == capacity
        a.buckets[0].append(("x", 1))
        assert b.buckets == [[] for _ in range(capacity)]
    assert len(HashTable().buckets) == 8
    for bad in [0, -1, True, 3.2]:
        try:
            HashTable(bad)
        except ValueError:
            pass
        else:
            assert False, "Reject invalid capacity"
