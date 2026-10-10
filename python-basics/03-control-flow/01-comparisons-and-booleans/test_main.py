import ast
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import solution as s


def _lines():
    output = StringIO()
    with redirect_stdout(output):
        exec(Path(s.__file__).read_text(), {})
    return output.getvalue().strip().splitlines()


def test_paint_comparisons():
    """1. Compare four paint tubes"""
    assert s.paint_tubes == 4, "Set paint_tubes to 4"
    assert _lines()[:2] == ["False", "False"], "Keep both paint comparisons"


def test_combined_checks():
    """2. Combine checks with one paper pack"""
    assert s.paper_packs == 1, "Set paper_packs to 1"
    assert _lines()[2:] == ["False", "True", "True"], "Keep and, or, and not checks"
    tree = ast.parse(Path(s.__file__).read_text())
    for kind in (ast.And, ast.Or, ast.Not):
        assert any(isinstance(n, kind) for n in ast.walk(tree)), "Keep the logical operators"
