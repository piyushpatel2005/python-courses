from solution import *
import ast
import solution

def test_room():
    """Update the map location and its displayed label"""
    assert room == "Beacon Ridge", "Assign Beacon Ridge to room"
    source_path = solution.__file__
    assert source_path is not None
    with open(source_path, encoding="utf-8") as source_file:
        tree = ast.parse(source_file.read())
    assert any(
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "print"
        and len(node.args) == 1
        and isinstance(node.args[0], ast.Name)
        and node.args[0].id == "room"
        for node in ast.walk(tree)
    ), "Keep print(room) so the updated map label appears when you Run."
