import ast
from pathlib import Path
import solution as s

def test_skip_canceled_order():
    tree = ast.parse(Path(s.__file__).read_text())
    assert any(isinstance(n, ast.Continue) for n in ast.walk(tree)), "Use continue to skip order 3"
    assert s.processed_orders.startswith("1 2 4 ") and "3 " not in s.processed_orders, "Process orders 1, 2, and 4 before any others"

def test_stop_at_daily_limit():
    tree = ast.parse(Path(s.__file__).read_text())
    assert any(isinstance(n, ast.Break) for n in ast.walk(tree)), "Use break once daily_limit is reached"
    assert (s.processed_orders, s.processed_count) == ("1 2 4 ", 3), "Stop after three valid orders"
