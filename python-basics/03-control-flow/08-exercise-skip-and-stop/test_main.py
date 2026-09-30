import ast
from pathlib import Path
import solution as s

def test_skip_invalid_visitor():
    tree = ast.parse(Path(s.__file__).read_text())
    assert any(isinstance(n, ast.Continue) for n in ast.walk(tree)), "Use continue to skip visitor 3"
    assert s.admitted.startswith("1 2 4 ") and "3 " not in s.admitted, "Admit visitors 1, 2, and 4 before any others"

def test_stop_at_capacity():
    tree = ast.parse(Path(s.__file__).read_text())
    assert any(isinstance(n, ast.Break) for n in ast.walk(tree)), "Use break once capacity is reached"
    assert (s.admitted, s.count) == ("1 2 4 ", 3), "Stop after three valid visitors"
