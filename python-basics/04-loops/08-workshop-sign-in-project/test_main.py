import ast
from pathlib import Path
import solution as s


def test_skip_canceled_registration():
    tree = ast.parse(Path(s.__file__).read_text())
    assert any(isinstance(n, ast.Continue) for n in ast.walk(tree)), "Skip registration 2 using continue"
    assert s.checked_in.startswith("1 3 ") and "2 " not in s.checked_in, "Check in registrations 1 and 3, but not 2"


def test_stop_at_capacity():
    tree = ast.parse(Path(s.__file__).read_text())
    assert any(isinstance(n, ast.Break) for n in ast.walk(tree)), "Stop check-in with break"
    assert (s.checked_in, s.attendee_count) == ("1 3 ", 2), "Stop after two valid registration IDs"


def test_report_capacity_status():
    source = Path(s.__file__).read_text()
    tree = ast.parse(source)
    assert any(isinstance(n, ast.If) and n.orelse for n in tree.body), "Choose the status after the loop using if/else"
    assert s.status == "Full", "Report Full for capacity 2"
    variant = ast.parse(source)
    variant.body[0].value = ast.Constant(value=8)
    scope = {}
    exec(compile(ast.fix_missing_locations(variant), "variant.py", "exec"), scope)
    assert (scope.get("checked_in"), scope.get("attendee_count"), scope.get("status")) == ("1 3 4 5 6 ", 5, "Spaces left"), "Report Spaces left when capacity exceeds valid registrations"
