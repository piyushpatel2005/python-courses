from solution import *

def _check_technique():
    import ast
    import solution
    with open(solution.__file__, encoding="utf-8") as source_file:
        tree = ast.parse(source_file.read())
    forbidden = ['hash']
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
    "Complete `validate_capacity` to accept positive integers other than bool and reject everything else with `ValueError`."
    for bad in [0, -2, True, 2.5, "4"]:
        try: validate_capacity(bad)
        except ValueError: pass
        else: assert False, "Reject invalid capacity"
    assert validate_capacity(1) is None


def test_02_complete_behavior():
    "Complete `bucket_index` to call validation and fold the string characters into a rolling bucket index."
    _check_technique()
    for key in ["", "A", "ab", "ba", "café", "木", "rack" * 10]:
        for capacity in [1, 2, 7, 19]:
            expected = 0
            for char in key: expected = (31 * expected + ord(char)) % capacity
            assert bucket_index(key, capacity) == expected
    for bad in [0, -3, True, 2.5]:
        try:
            bucket_index("x", bad)
        except ValueError:
            pass
        else:
            assert False, "Reject invalid capacity"
