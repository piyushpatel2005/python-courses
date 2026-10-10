import ast
from pathlib import Path
import solution as s


def test_skip_unsafe_tile():
    tree = ast.parse(Path(s.__file__).read_text())
    assert any(isinstance(n, ast.Continue) for n in ast.walk(tree)), "Skip tile 2 using continue"
    assert s.path.startswith("1 3 ") and "2 " not in s.path, "Issue tiles 1 and 3, but not 2"


def test_stop_at_capacity():
    tree = ast.parse(Path(s.__file__).read_text())
    assert any(isinstance(n, ast.Break) for n in ast.walk(tree)), "Stop mapping path with break"
    assert (s.path, s.steps) == ("1 3 ", 2), "Stop after two valid path"


def test_report_full_and_open():
    source = Path(s.__file__).read_text()
    tree = ast.parse(source)
    assert any(isinstance(n, ast.If) and n.orelse for n in tree.body), "Choose the gate_status after the loop using if/else"
    assert s.gate_status == "Unlocked", "Report Unlocked for gate_limit 2"
    variant = ast.parse(source)
    variant.body[0].value = ast.Constant(value=8)
    scope = {}
    exec(compile(ast.fix_missing_locations(variant), "variant.py", "exec"), scope)
    assert (scope.get("path"), scope.get("steps"), scope.get("gate_status")) == ("1 3 4 5 6 ", 5, "Sealed"), "Report Sealed when gate_limit exceeds safe tiles"
