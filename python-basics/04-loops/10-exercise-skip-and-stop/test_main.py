import ast
from pathlib import Path
import solution as s

def test_skip_unsafe_tile():
    tree = ast.parse(Path(s.__file__).read_text())
    assert any(isinstance(n, ast.Continue) for n in ast.walk(tree)), "Use continue to skip tile 3"
    assert s.safe_tiles.startswith("1 2 4 ") and "3 " not in s.safe_tiles, "Clear tiles 1, 2, and 4 before any others"

def test_stop_at_capacity():
    tree = ast.parse(Path(s.__file__).read_text())
    assert any(isinstance(n, ast.Break) for n in ast.walk(tree)), "Use break once route_limit is reached"
    assert (s.safe_tiles, s.cleared_count) == ("1 2 4 ", 3), "Stop after three valid tiles"
