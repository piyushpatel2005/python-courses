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
    "Raise `KeyError(key)` after a bucket scan finds no equal key."
    table = HashTable(1)
    table.put("present", 4)
    for key in ["missing", ""]:
        try: table.get(key)
        except KeyError as error: assert error.args == (key,)
        else: assert False, "Report the absent key"
    assert table.size == 1


def test_02_complete_behavior():
    "Return the value from an equal pair without changing the table."
    _check_technique()
    table = HashTable(1)
    payload = []
    for key, value in [("a", None), ("b", 0), ("c", payload)]: table.put(key, value)
    saved = [bucket[:] for bucket in table.buckets]
    assert table.get("a") is None and table.get("b") == 0
    assert table.get("c") is payload
    for key in ["missing", ""]:
        try:
            table.get(key)
        except KeyError as error:
            assert error.args == (key,)
        else:
            assert False, "Missing keys must raise KeyError"
    assert table.buckets == saved and table.size == 3
    distributed = HashTable(7)
    for key in ["a", "b", "c", "h"]: distributed.put(key, key)
    for key in ["a", "b", "c", "h"]: assert distributed.get(key) == key
    try:
        distributed.get("empty-bucket-key")
    except KeyError:
        pass
    else:
        assert False, "Missing keys may land in any bucket"
