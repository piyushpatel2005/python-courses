import ast
from pathlib import Path
import solution as _sol


def test_collect_three_valid_marks():
    """Skip a damaged rune and stop after three marks."""
    tree = ast.parse(Path(_sol.__file__).read_text())
    assert any(isinstance(node, ast.Continue) for node in ast.walk(tree)), "Skip rune 3 using continue"
    assert any(isinstance(node, ast.Break) for node in ast.walk(tree)), "Stop collecting marks using break"
    assert _sol.marks == "1 2 4 ", "Collect runes 1, 2, and 4 in order"
    assert _sol.collected == 3, "Count only the three collected marks"


def test_report_gate_status():
    """Report Unlocked after the third mark."""
    tree = ast.parse(Path(_sol.__file__).read_text())
    assert any(isinstance(node, ast.If) for node in tree.body), "Use if/else after the loop"
    assert _sol.gate_status == "Unlocked", "Set gate_status to Unlocked when enough marks are collected"
