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
    for oil, keys in ((6, 1), (3, 1), (4, 0), (4, 1), (8, 3)):
        variant = ast.parse(source)
        for node in variant.body:
            if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
                if node.targets[0].id == "oil_units":
                    node.value = ast.Constant(value=oil)
                elif node.targets[0].id == "key_count":
                    node.value = ast.Constant(value=keys)
        scope = {}
        with redirect_stdout(StringIO()):
            exec(compile(ast.fix_missing_locations(variant), "variant.py", "exec"), scope)
        assert scope.get(name) is expected(oil, keys), f"Check {name} with oil={oil} and keys={keys}"


def test_enough_oil():
    """1. Compare oil with the minimum."""
    _check("enough_oil", lambda oil, keys: oil >= 4)


def test_has_key():
    """2. Compare keys with the minimum."""
    _check("has_key", lambda oil, keys: keys >= 1)
