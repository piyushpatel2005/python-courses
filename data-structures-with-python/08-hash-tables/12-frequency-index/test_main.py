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
    "Complete `increment_count` to create a count of one or increase an existing count."
    table = HashTable(3)
    increment_count(table, "oak")
    assert table.get("oak") == 1 and table.size == 1
    increment_count(table, "oak")
    increment_count(table, "Oak")
    assert table.get("oak") == 2 and table.get("Oak") == 1 and table.size == 2


def test_02_complete_behavior():
    "Complete `frequency_index` to create the sized table and apply that helper to each word."
    _check_technique()
    words = ["oak", "elm", "oak", "", "Oak", "elm", "oak"]
    saved = words[:]
    table = frequency_index(words)
    assert isinstance(table, HashTable) and len(table.buckets) == 2 * len(words)
    assert sorted(table.entries()) == [("", 1), ("Oak", 1), ("elm", 2), ("oak", 3)]
    assert table.size == 4 and words == saved
    empty = frequency_index([])
    assert empty.entries() == [] and len(empty.buckets) == 1
    other = frequency_index(["oak"])
    assert other.get("oak") == 1 and table.get("oak") == 3
