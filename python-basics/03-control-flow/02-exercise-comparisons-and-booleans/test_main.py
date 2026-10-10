import ast
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import solution as s


def _check(name, technique, expected):
    source = Path(s.__file__).read_text()
    tree = ast.parse(source)
    assignment = next((n for n in tree.body if isinstance(n, ast.Assign)
                       and any(isinstance(t, ast.Name) and t.id == name for t in n.targets)), None)
    assert assignment is not None, f"Keep the {name} assignment"
    assert any(isinstance(n, technique) for n in ast.walk(assignment.value)), "Use the requested comparison or logical operator"
    for oil, keys, closed in ((6, 1, True), (3, 1, False), (4, 0, True), (4, 1, False)):
        variant = ast.parse(source)
        values = {"oil_units": oil, "key_count": keys, "gate_closed": closed}
        # Supply the earlier task's result independently for the and task.
        if name == "can_enter":
            values["enough_oil"] = oil >= 4
        for node in variant.body:
            if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
                key = node.targets[0].id
                if key in values:
                    node.value = ast.Constant(value=values[key])
        scope = {}
        with redirect_stdout(StringIO()):
            exec(compile(ast.fix_missing_locations(variant), "variant.py", "exec"), scope)
        assert scope.get(name) is expected(oil, keys, closed), f"Check {name} for oil={oil}, keys={keys}, closed={closed}"


def test_enough_oil():
    """1. Compare oil with the minimum"""
    _check("enough_oil", ast.Compare, lambda oil, keys, closed: oil >= 4)


def test_can_enter():
    """2. Require oil and a key"""
    _check("can_enter", ast.And, lambda oil, keys, closed: oil >= 4 and keys >= 1)


def test_needs_supplies():
    """3. Detect either missing supply"""
    _check("needs_supplies", ast.Or, lambda oil, keys, closed: oil < 4 or keys == 0)


def test_gate_open():
    """4. Reverse the closed flag"""
    _check("gate_open", ast.Not, lambda oil, keys, closed: not closed)
