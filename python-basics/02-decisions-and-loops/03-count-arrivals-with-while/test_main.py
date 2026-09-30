import ast
from pathlib import Path
import solution as _sol


def test_count_all_arrivals():
    """A terminating while loop checks three tickets"""
    tree = ast.parse(Path(_sol.__file__).read_text())
    assert any(isinstance(node, ast.While) for node in tree.body), "Use a while loop"
    assert _sol.checked == 3, "Check tickets 1, 2, and 3 exactly once"
    assert _sol.ticket == 4, "Advance ticket so the loop stops after ticket 3"
