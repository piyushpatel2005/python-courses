import ast
from pathlib import Path
import solution as _sol


def test_count_gate_pulses():
    """A terminating while loop charges the gate with three pulses."""
    tree = ast.parse(Path(_sol.__file__).read_text())
    assert any(isinstance(node, ast.While) for node in tree.body), "Use a while loop"
    assert _sol.charged == 3, "Count pulses 1, 2, and 3 exactly once"
    assert _sol.pulse == 4, "Advance pulse so the loop stops after pulse 3"
