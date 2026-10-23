import ast
from pathlib import Path
import solution as s

def test_even_hours():
    tree = ast.parse(Path(s.__file__).read_text())
    assert any(isinstance(n, ast.For) and isinstance(n.iter, ast.Call) and isinstance(n.iter.func, ast.Name) and n.iter.func.id == "range" for n in tree.body), "Loop over a range"
    assert s.labels == "Hour 2 | Hour 4 | Hour 6 | ", "Label hours 2, 4, and 6"
