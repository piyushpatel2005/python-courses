import ast
import inspect
import textwrap
from solution import total_attendance, save_attendance, read_attendance

def test_total_attendance():
    """Add valid headcounts and skip invalid text."""
    assert total_attendance(["2", "bad", "4"]) == 6
    assert total_attendance([]) == 0
    assert total_attendance(["9", "no", "2", "0"]) == 11
    tree = ast.parse(textwrap.dedent(inspect.getsource(total_attendance)))
    assert any(isinstance(n, ast.For) for n in ast.walk(tree)), "Use a loop to process entries."
    assert any(isinstance(n, ast.ExceptHandler) and isinstance(n.type, ast.Name) and n.type.id == "ValueError" for n in ast.walk(tree)), "Catch ValueError for invalid counts."

def test_save_attendance():
    """Save the calculated total, not a fixed example."""
    save_attendance(["5", "oops", "1"])
    with open("attendance-log.txt", "r", encoding="utf-8") as file:
        assert file.read() == "Attendees: 6"
    original = save_attendance.__globals__["total_attendance"]
    calls = []
    def tracked(entries):
        calls.append(entries)
        return 37
    try:
        save_attendance.__globals__["total_attendance"] = tracked
        save_attendance(["new", "entries"])
        assert calls == [["new", "entries"]], "Call total_attendance(entries)."
        with open("attendance-log.txt", "r", encoding="utf-8") as file:
            assert file.read() == "Attendees: 37"
    finally:
        save_attendance.__globals__["total_attendance"] = original

def test_read_attendance():
    """Read every character from the file."""
    with open("attendance-log.txt", "w", encoding="utf-8") as file:
        file.write("Friday\nAttendees: 7")
    assert read_attendance() == "Friday\nAttendees: 7"
