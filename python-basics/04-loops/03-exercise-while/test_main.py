import ast
from pathlib import Path
import solution as s

def test_bounded_packing():
    tree = ast.parse(Path(s.__file__).read_text())
    assert any(isinstance(n, ast.While) for n in tree.body), "Use a while loop"
    assert (s.boxes_packed, s.packing_rounds) == (40, 3), "Pack boxes from 10 to 40 in three rounds"
