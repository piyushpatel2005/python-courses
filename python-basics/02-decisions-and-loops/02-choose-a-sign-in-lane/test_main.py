import ast
from pathlib import Path
import solution as _sol


def test_sign_in_lanes():
    """Choose the correct lane for empty, nearly full, and open sessions"""
    tree = ast.parse(Path(_sol.__file__).read_text())
    branches = [node for node in tree.body if isinstance(node, ast.If)]
    assert branches, "Use an if statement to choose the lane"
    assert branches[0].orelse, "Add an elif branch"
    assert isinstance(branches[0].orelse[0], ast.If), "Add an elif branch"
    assert branches[0].orelse[0].orelse, "Add an else branch"
    source = Path(_sol.__file__).read_text()
    for seats, expected in ((0, "Waitlist"), (2, "Last seats"), (8, "Open")):
        # Override only the supplied starting value; run the learner's actual branches.
        variant = ast.parse(source)
        first = variant.body[0]
        assert isinstance(first, ast.Assign) and first.targets[0].id == "seats_left"
        first.value = ast.Constant(value=seats)
        scope = {}
        exec(compile(ast.fix_missing_locations(variant), "solution.py", "exec"), scope)
        assert scope.get("lane") == expected, f"With {seats} seats left, lane should be {expected!r}"
