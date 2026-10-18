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
    for oil, keys, closed in ((6, 1, True), (3, 1, False), (4, 0, True), (4, 1, False), (6, 0, False)):
        variant = ast.parse(source)
        for node in variant.body:
            if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
                key = node.targets[0].id
                if key in ("oil_units", "key_count", "gate_closed"):
                    node.value = ast.Constant(value={"oil_units": oil, "key_count": keys, "gate_closed": closed}[key])
        scope = {}
        with redirect_stdout(StringIO()):
            exec(compile(ast.fix_missing_locations(variant), "variant.py", "exec"), scope)
        assert scope.get(name) is expected(oil, keys, closed), \
            f"Check {name} with oil={oil}, keys={keys}, closed={closed}"


def test_can_enter():
    """1. Require both oil and a key."""
    _check("can_enter", ast.And, lambda oil, keys, closed: oil >= 4 and keys >= 1)


def test_needs_supplies():
    """2. Detect either missing supply."""
    _check("needs_supplies", ast.Or, lambda oil, keys, closed: oil < 4 or keys == 0)


def test_gate_open():
    """3. Reverse the closed flag."""
    _check("gate_open", ast.Not, lambda oil, keys, closed: not closed)
