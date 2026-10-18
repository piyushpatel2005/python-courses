import ast
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import solution as s


def _lines():
    assert s.__file__ is not None
    tree = ast.parse(Path(s.__file__).read_text())
    assert all(any(isinstance(n, kind) for n in ast.walk(tree))
               for kind in (ast.And, ast.Or, ast.Not)), "Keep all three logical checks"
    output = StringIO()
    with redirect_stdout(output):
        exec(compile(tree, s.__file__, "exec"), {})
    return output.getvalue().strip().splitlines()


def test_paper_packs():
    """1. See what one paper pack changes."""
    assert getattr(s, "paper_packs") == 1, "Set paper_packs to 1"
    assert _lines()[:2] == ["False", "True"], "Keep the and and or checks"


def test_markers():
    """2. See what no markers changes."""
    assert getattr(s, "markers") == 0, "Set markers to 0"
    assert _lines()[2] == "False", "Keep the not check"
