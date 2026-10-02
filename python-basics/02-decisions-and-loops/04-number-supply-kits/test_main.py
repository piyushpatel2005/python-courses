import ast
from pathlib import Path
import solution as _sol


def test_four_numbered_markers():
    """A for/range loop builds four ordered beacon markers."""
    tree = ast.parse(Path(_sol.__file__).read_text())
    assert any(isinstance(node, ast.For) and isinstance(node.iter, ast.Call)
               and isinstance(node.iter.func, ast.Name) and node.iter.func.id == "range"
               for node in tree.body), "Use for ... in range(...)"
    assert _sol.markers == "Marker 1; Marker 2; Marker 3; Marker 4; ", "Label markers 1 to 4 in order"
