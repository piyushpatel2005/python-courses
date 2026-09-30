import ast
from pathlib import Path
import solution as s

def test_even_stops():
    tree = ast.parse(Path(s.__file__).read_text())
    assert any(isinstance(n, ast.For) and isinstance(n.iter, ast.Call) and isinstance(n.iter.func, ast.Name) and n.iter.func.id == "range" for n in tree.body), "Loop over a range"
    assert s.labels == "Stop 2 | Stop 4 | Stop 6 | ", "Label stops 2, 4, and 6"
