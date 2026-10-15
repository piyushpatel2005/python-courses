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
    "Complete `empty_buckets` to validate capacity and return independent empty bucket lists."
    buckets = empty_buckets(3)
    assert buckets == [[], [], []]
    buckets[0].append("a")
    assert buckets[1:] == [[], []]
    try: empty_buckets(0)
    except ValueError: pass
    else: assert False, "Call the supplied validator"


def test_02_complete_behavior():
    "Complete `collision_buckets` to append every key occurrence to its computed bucket."
    _check_technique()
    keys = ["a", "h", "a", "", "z"]
    for capacity in [1, 3, 7]:
        result = collision_buckets(keys, capacity)
        expected = [[] for _ in range(capacity)]
        for key in keys: expected[bucket_index(key, capacity)].append(key)
        assert result == expected
        assert len({id(bucket) for bucket in result}) == capacity
    assert keys == ["a", "h", "a", "", "z"]
    assert collision_buckets([], 3) == [[], [], []]
    try:
        collision_buckets([], 0)
    except ValueError:
        pass
    else:
        assert False, "Validate even without keys"
