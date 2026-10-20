import ast
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import solution as s


def _tree():
    assert s.__file__ is not None
    return ast.parse(Path(s.__file__).read_text(encoding="utf-8"))


def _chain():
    branches = [node for node in _tree().body if isinstance(node, ast.If)]
    assert branches, "Add an if statement below seat_message."
    return branches[0]


def _run_with_seats(seats):
    tree = _tree()
    supplied = next((node for node in tree.body if isinstance(node, ast.Assign)
                     and any(isinstance(t, ast.Name) and t.id == "seats_left" for t in node.targets)), None)
    assert supplied is not None, "Keep the supplied seats_left assignment."
    supplied.value = ast.Constant(value=seats)
    scope = {}
    output = StringIO()
    with redirect_stdout(output):
        exec(compile(ast.fix_missing_locations(tree), "submission.py", "exec"), scope)
    return scope.get("seat_message"), output.getvalue().strip()


def _expect(seats, message):
    actual, output = _run_with_seats(seats)
    assert actual == message, f"With {seats} seats left, set seat_message to {message!r}."
    assert output == message, "Keep print(seat_message) below the whole branch chain."


def test_sold_out():
    """1. Report sold out when no seats remain."""
    _chain()
    _expect(0, "Sold out")
    assert _run_with_seats(8)[0] != "Sold out", "Use == 0 for sold-out events."


def test_few_seats():
    """2. Report when fewer than four seats remain."""
    first = _chain()
    assert first.orelse and isinstance(first.orelse[0], ast.If), "Add an elif branch after the zero-seat case."
    for seats in (1, 2, 3):
        _expect(seats, "Few seats left")
    assert _run_with_seats(4)[0] != "Few seats left", "Four seats belong in the last branch."


def test_seats_available():
    """3. Report when at least four seats remain."""
    first = _chain()
    assert first.orelse and isinstance(first.orelse[0], ast.If), "Keep the if/elif chain."
    middle = first.orelse[0]
    assert middle.orelse and not isinstance(middle.orelse[0], ast.If), "Add an else branch."
    for seats in (4, 8, 20):
        _expect(seats, "Seats available")
    assert _run_with_seats(3)[0] != "Seats available", "Three seats belong in the middle branch."
