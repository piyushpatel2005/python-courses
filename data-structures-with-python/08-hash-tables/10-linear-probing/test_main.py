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
    "Complete `probe_slot` to wrap a home index plus an offset into the slot range."
    assert [probe_slot(4, offset, 5) for offset in range(5)] == [4, 0, 1, 2, 3]
    assert probe_slot(0, 0, 1) == 0


def test_02_step():
    "Report a missing key at an untouched slot or after a full unsuccessful probe cycle."
    for capacity in [1, 4]:
        table = ProbingTable(capacity)
        for key in ["empty"]:
            try: table.get(key)
            except KeyError: pass
            else: assert False, "Missing empty-slot lookup"
        for i in range(capacity): table.put(str(i), i)
        try: table.get("not-stored")
        except KeyError: pass
        else: assert False, "Stop after a full unsuccessful cycle"


def test_03_complete_behavior():
    "Return an equal live pair's value, continuing past collisions and tombstones."
    _check_technique()
    table = ProbingTable(4)
    for key, value in [("c", None), ("g", 0), ("k", 3), ("o", 4)]: table.put(key, value)
    assert table.get("c") is None and table.get("g") == 0
    assert table.get("k") == 3 and table.get("o") == 4
    saved = table.slots[:]
    for key in ["s", "absent"]:
        try:
            table.get(key)
        except KeyError as error:
            assert error.args == (key,)
        else:
            assert False, "Missing lookup must terminate even when full"
    assert table.slots == saved and table.size == 4
    empty = ProbingTable(1)
    try:
        empty.get("x")
    except KeyError:
        pass
    else:
        assert False, "An untouched slot means missing"
    import solution
    table.slots[bucket_index("c", 4)] = solution._DELETED
    table.size -= 1
    assert table.get("g") == 0 and table.get("o") == 4
    try:
        table.get("c")
    except KeyError:
        pass
    else:
        assert False, "Skip tombstones without treating them as live entries"
