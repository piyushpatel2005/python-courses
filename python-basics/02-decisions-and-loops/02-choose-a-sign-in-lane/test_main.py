import ast
from pathlib import Path
import solution as _sol


def test_gate_signals():
    """Choose the gate signal for no, low, and ample charge."""
    source = Path(_sol.__file__).read_text()
    tree = ast.parse(source)
    branches = [node for node in tree.body if isinstance(node, ast.If)]
    assert branches, "Use an if statement to choose the gate signal"
    assert branches[0].orelse and isinstance(branches[0].orelse[0], ast.If), "Add an elif branch"
    assert branches[0].orelse[0].orelse, "Add an else branch"
    for charge, expected in ((0, "Sealed"), (2, "Flickering"), (8, "Open")):
        variant = ast.parse(source)
        first = variant.body[0]
        assert isinstance(first, ast.Assign) and first.targets[0].id == "charge_left"
        first.value = ast.Constant(value=charge)
        scope = {}
        exec(compile(ast.fix_missing_locations(variant), "solution.py", "exec"), scope)
        assert scope.get("gate_signal") == expected, f"With charge {charge}, gate_signal should be {expected!r}"
