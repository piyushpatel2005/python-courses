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
    "Return `False` when a bounded probe finds no live equal key."
    table = ProbingTable(3)
    table.put("a", 1)
    assert table.delete("missing") is False and table.size == 1
    assert table.get("a") == 1


def test_02_step():
    "Replace an equal live pair with `_DELETED` and return `True`."
    table = ProbingTable(4)
    table.put("c", 1); table.put("g", 2)
    assert table.delete("c") is True and table.get("g") == 2
    assert table.delete("c") is False
    import solution
    assert table.slots[bucket_index("c", 4)] is solution._DELETED


def test_03_complete_behavior():
    "Reduce size only when a live pair was marked deleted."
    _check_technique()
    table = ProbingTable(4)
    for key in ["c", "g", "k", "o"]: table.put(key, key)
    assert table.delete("c") is True and table.size == 3
    assert table.get("g") == "g" and table.get("o") == "o"
    assert table.delete("c") is False and table.size == 3
    table.put("k", "updated")
    assert table.size == 3 and table.get("k") == "updated"
    table.put("s", 9)
    assert table.size == 4 and table.get("s") == 9
    for key in ["g", "k", "o", "s"]: assert table.delete(key) is True
    assert table.size == 0 and table.delete("missing") is False
    table.put("new", None)
    assert table.size == 1 and table.get("new") is None
    assert table.delete("new") is True
    try:
        table.get("new")
    except KeyError:
        pass
    else:
        assert False, "Deleted keys must be absent"
