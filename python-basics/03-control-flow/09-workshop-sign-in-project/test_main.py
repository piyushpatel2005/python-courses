import ast
from pathlib import Path
import solution as s


def test_skip_invalid_ticket():
    tree = ast.parse(Path(s.__file__).read_text())
    assert any(isinstance(n, ast.Continue) for n in ast.walk(tree)), "Skip ticket 2 using continue"
    assert s.passes.startswith("1 3 ") and "2 " not in s.passes, "Issue tickets 1 and 3, but not 2"


def test_stop_at_capacity():
    tree = ast.parse(Path(s.__file__).read_text())
    assert any(isinstance(n, ast.Break) for n in ast.walk(tree)), "Stop issuing passes with break"
    assert (s.passes, s.issued) == ("1 3 ", 2), "Stop after two valid passes"


def test_report_full_and_open():
    source = Path(s.__file__).read_text()
    tree = ast.parse(source)
    assert any(isinstance(n, ast.If) and n.orelse for n in tree.body), "Choose the status after the loop using if/else"
    assert s.status == "Full", "Report Full for capacity 2"
    variant = ast.parse(source)
    variant.body[0].value = ast.Constant(value=8)
    scope = {}
    exec(compile(ast.fix_missing_locations(variant), "variant.py", "exec"), scope)
    assert (scope.get("passes"), scope.get("issued"), scope.get("status")) == ("1 3 4 5 6 ", 5, "Open"), "Report Open when capacity exceeds available tickets"
