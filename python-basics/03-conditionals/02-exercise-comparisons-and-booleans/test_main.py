import ast
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import solution as s


def _check(name, expected):
    assert s.__file__ is not None
    source = Path(s.__file__).read_text()
    tree = ast.parse(source)
    assignment = next((n for n in tree.body if isinstance(n, ast.Assign)
                       and any(isinstance(t, ast.Name) and t.id == name for t in n.targets)), None)
    assert assignment is not None and isinstance(assignment.value, ast.Compare), \
        f"Write a comparison for {name}"
    for flour, cartons in ((6, 1), (3, 1), (4, 0), (4, 1), (8, 3)):
        variant = ast.parse(source)
        for node in variant.body:
            if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
                if node.targets[0].id == "flour_bags":
                    node.value = ast.Constant(value=flour)
                elif node.targets[0].id == "milk_cartons":
                    node.value = ast.Constant(value=cartons)
        scope = {}
        with redirect_stdout(StringIO()):
            exec(compile(ast.fix_missing_locations(variant), "variant.py", "exec"), scope)
        assert scope.get(name) is expected(flour, cartons), f"Check {name} with flour={flour} and cartons={cartons}"


def test_enough_flour():
    """1. Compare flour with the minimum."""
    _check("enough_flour", lambda flour, cartons: flour >= 4)


def test_has_milk():
    """2. Compare cartons with the minimum."""
    _check("has_milk", lambda flour, cartons: cartons >= 1)
