import ast
import inspect
import textwrap
from solution import parse_command, book_seats, all_full, registration_report


def test_parse_command():
    """Valid requests decode; invalid quantities do not crash."""
    assert parse_command(" pottery:2 ") == ("POTTERY", 2)
    assert parse_command("DRAWING:5") == ("DRAWING", 5)
    for bad in ("oops", ":3", "POTTERY:no", "POTTERY:0", "POTTERY:-2", "POTTERY:3:4"):
        assert parse_command(bad) is None, f"Ignore {bad!r}."
    tree = ast.parse(textwrap.dedent(inspect.getsource(parse_command)))
    assert any(isinstance(node, ast.Try) and any(isinstance(handler.type, ast.Name)
               and handler.type.id == "ValueError" for handler in node.handlers if handler.type)
               for node in ast.walk(tree)), "Catch ValueError for a bad quantity."


def test_book_seats():
    """Only valid known requests are booked, without overselling."""
    workshops = {"POTTERY": 3, "DRAWING": 2, "SEWING": 4}
    assert book_seats(workshops, ["pottery:2", "bad", "POTTERY:1", "dance:9", "drawing:2"]) == {
        "POTTERY": 3, "DRAWING": 2, "SEWING": 0}
    assert book_seats({"PAINTING": 5}, ["painting:4", "painting:2", "painting:-2", "painting:1"]) == {"PAINTING": 5}
    assert book_seats({"POTTERY": 3}, ["POTTERY:4", "POTTERY:2"]) == {"POTTERY": 2}
    assert workshops == {"POTTERY": 3, "DRAWING": 2, "SEWING": 4}
    namespace = book_seats.__globals__
    original = namespace["parse_command"]
    try:
        namespace["parse_command"] = lambda command: ("POTTERY", 2) if command == "probe" else None
        assert book_seats({"POTTERY": 3}, ["probe"]) == {"POTTERY": 2}, (
            "Use parse_command inside book_seats.")
    finally:
        namespace["parse_command"] = original


def test_all_full():
    """Every listed workshop needs all its seats booked."""
    assert all_full({"POTTERY": 3, "DRAWING": 2}, {"POTTERY": 3, "DRAWING": 2}) is True
    assert all_full({"POTTERY": 3, "DRAWING": 2}, {"POTTERY": 3, "DRAWING": 1}) is False
    assert all_full({"POTTERY": 3}, {}) is False
    assert all_full({}, {}) is False
    tree = ast.parse(textwrap.dedent(inspect.getsource(all_full)))
    assert any(isinstance(n, ast.For) for n in ast.walk(tree)), "Check every workshop with a loop."
    assert any(isinstance(n, ast.If) for n in ast.walk(tree)), "Use a condition for capacity."


def test_registration_report():
    """The report shows workshop and overall totals with the right status."""
    workshops = {"POTTERY": 3, "DRAWING": 2}
    assert registration_report(workshops, ["pottery:2", "POTTERY:1", "drawing:2"]) == [
        "POTTERY: 3/3 seats booked", "DRAWING: 2/2 seats booked",
        "Total seats: 5/5 booked",
        "Registration: FULL - All workshop seats are booked."]
    assert registration_report(workshops, ["pottery:3", "drawing:1"]) == [
        "POTTERY: 3/3 seats booked", "DRAWING: 1/2 seats booked",
        "Total seats: 4/5 booked",
        "Registration: OPEN - Seats are still available."]
    assert registration_report({}, []) == [
        "Total seats: 0/0 booked", "Registration: NO WORKSHOPS - Add a workshop first."]
    namespace = registration_report.__globals__
    original_book, original_full = namespace["book_seats"], namespace["all_full"]
    try:
        namespace["book_seats"] = lambda workshops, commands: {"POTTERY": 2}
        namespace["all_full"] = lambda workshops, bookings: False
        assert registration_report({"POTTERY": 9}, ["probe"]) == [
            "POTTERY: 2/9 seats booked", "Total seats: 2/9 booked",
            "Registration: OPEN - Seats are still available."], (
            "Reuse book_seats and all_full inside registration_report.")
    finally:
        namespace["book_seats"], namespace["all_full"] = original_book, original_full
