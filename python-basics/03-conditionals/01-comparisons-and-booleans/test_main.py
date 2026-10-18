import ast
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import solution as s


def test_paint_comparisons():
    """Change the paint supply and keep both comparisons."""
    assert s.__file__ is not None
    assert getattr(s, "paint_tubes") == 4, "Set paint_tubes to 4"
    tree = ast.parse(Path(s.__file__).read_text())
    checks = [n for n in ast.walk(tree) if isinstance(n, ast.Compare)]
    assert len(checks) >= 2, "Keep both paint comparisons"
    output = StringIO()
    with redirect_stdout(output):
        exec(compile(tree, s.__file__, "exec"), {})
    assert output.getvalue().strip().splitlines() == ["False", "False"]
