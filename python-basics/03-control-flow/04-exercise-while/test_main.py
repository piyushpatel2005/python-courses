import ast
from pathlib import Path
import solution as s

def test_bounded_charging():
    tree = ast.parse(Path(s.__file__).read_text())
    assert any(isinstance(n, ast.While) for n in tree.body), "Use a while loop"
    assert (s.charge, s.steps) == (40, 3), "Charge from 10 to 40 in three steps"
