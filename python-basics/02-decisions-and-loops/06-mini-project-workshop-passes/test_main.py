import ast
from pathlib import Path
import solution as _sol


def test_issue_three_valid_passes():
    """Skip the unusable ticket and stop after three passes"""
    tree = ast.parse(Path(_sol.__file__).read_text())
    assert any(isinstance(node, ast.Continue) for node in ast.walk(tree)), "Skip ticket 3 using continue"
    assert any(isinstance(node, ast.Break) for node in ast.walk(tree)), "Stop issuing passes using break"
    assert _sol.passes == "1 2 4 ", "Issue tickets 1, 2, and 4 in order"
    assert _sol.issued == 3, "Count only the three issued passes"


def test_report_capacity():
    """Report Full after the third pass"""
    tree = ast.parse(Path(_sol.__file__).read_text())
    assert any(isinstance(node, ast.If) for node in tree.body), "Use if/else after the loop"
    assert _sol.desk_status == "Full", "Set desk_status to Full when capacity is reached"
