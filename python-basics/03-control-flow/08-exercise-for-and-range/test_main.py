import ast
from pathlib import Path
import solution as s

def test_even_patrols():
    tree = ast.parse(Path(s.__file__).read_text())
    assert any(isinstance(n, ast.For) and isinstance(n.iter, ast.Call) and isinstance(n.iter.func, ast.Name) and n.iter.func.id == "range" for n in tree.body), "Loop over a range"
    assert s.labels == "Patrol 2 | Patrol 4 | Patrol 6 | ", "Label patrols 2, 4, and 6"
