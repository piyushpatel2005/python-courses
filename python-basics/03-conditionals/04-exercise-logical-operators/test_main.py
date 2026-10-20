import ast
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import solution as s


def _check(name, technique, expected):
    assert s.__file__ is not None
    source = Path(s.__file__).read_text()
    tree = ast.parse(source)
    assignment = next((n for n in tree.body if isinstance(n, ast.Assign)
                       and any(isinstance(t, ast.Name) and t.id == name for t in n.targets)), None)
    assert assignment is not None and any(isinstance(n, technique) for n in ast.walk(assignment.value)), \
        f"Use the requested logical operator for {name}"
    for flour, cartons, closed in ((6, 1, True), (3, 1, False), (4, 0, True), (4, 1, False), (6, 0, False)):
        variant = ast.parse(source)
        for node in variant.body:
            if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
                field = node.targets[0].id
                if field in ("flour_bags", "milk_cartons", "store_closed"):
                    node.value = ast.Constant(value={"flour_bags": flour, "milk_cartons": cartons, "store_closed": closed}[field])
        scope = {}
        with redirect_stdout(StringIO()):
            exec(compile(ast.fix_missing_locations(variant), "variant.py", "exec"), scope)
        assert scope.get(name) is expected(flour, cartons, closed), \
            f"Check {name} with flour bags={flour}, milk cartons={cartons}, closed={closed}"


def test_can_take_order():
    """1. Require both flour and a carton."""
    _check("can_take_order", ast.And, lambda flour, cartons, closed: flour >= 4 and cartons >= 1)


def test_needs_restock():
    """2. Detect either item needs restocking."""
    _check("needs_restock", ast.Or, lambda flour, cartons, closed: flour < 4 or cartons == 0)


def test_store_open():
    """3. Reverse the closed flag."""
    _check("store_open", ast.Not, lambda flour, cartons, closed: not closed)
