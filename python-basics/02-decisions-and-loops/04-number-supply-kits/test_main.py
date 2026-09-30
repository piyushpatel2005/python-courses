import ast
from pathlib import Path
import solution as _sol


def test_four_numbered_kits():
    """A for/range loop builds four ordered labels"""
    tree = ast.parse(Path(_sol.__file__).read_text())
    assert any(isinstance(node, ast.For) and isinstance(node.iter, ast.Call)
               and isinstance(node.iter.func, ast.Name) and node.iter.func.id == "range"
               for node in tree.body), "Use for ... in range(...)"
    assert _sol.labels == "Kit 1; Kit 2; Kit 3; Kit 4; ", "Label kits 1 to 4 in order"
