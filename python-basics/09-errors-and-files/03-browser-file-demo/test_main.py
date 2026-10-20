import ast
import inspect
import solution
from solution import note, saved_note

def test_note_round_trip():
    """Write the note and read the same text back."""
    assert note == "Order ready for pickup"
    assert saved_note == note
    tree = ast.parse(inspect.getsource(solution))
    calls = [node.func.attr for node in ast.walk(tree)
             if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)]
    assert "write" in calls and "read" in calls, "Write and read using the file methods."
    assignment = next(node for node in tree.body
                      if isinstance(node, ast.Assign) and any(
                          isinstance(target, ast.Name) and target.id == "note"
                          for target in node.targets))
    assignment.value = ast.Constant("Please use the side door")
    ast.fix_missing_locations(tree)
    scope = {"__name__": "file_round_trip_check"}
    exec(compile(tree, "file_round_trip_check", "exec"), scope)
    with open("pickup-note.txt", "r", encoding="utf-8") as file:
        assert file.read() == "Please use the side door", "Write the changed note to the file."
    assert scope["saved_note"] == "Please use the side door", "Read back the changed note."
