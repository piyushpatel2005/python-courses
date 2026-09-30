import ast
from pathlib import Path
import solution
from solution import upper_names, long_names

def test_upper_names():
    assert upper_names == ["LI", "MARA", "JO", "SOFIA"]
    tree = ast.parse(Path(solution.__file__).read_text())
    assert any(isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == "map" and any(isinstance(a, ast.Lambda) for a in n.args) for n in ast.walk(tree)), "Use map with a lambda."

def test_long_names():
    assert long_names == ["MARA", "SOFIA"]
    tree = ast.parse(Path(solution.__file__).read_text())
    assert any(isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == "filter" and any(isinstance(a, ast.Lambda) for a in n.args) for n in ast.walk(tree)), "Use filter with a lambda."
