from solution import *
import solution as _solution

def _output():
    from contextlib import redirect_stdout
    from io import StringIO
    from pathlib import Path
    output = StringIO()
    with redirect_stdout(output):
        exec(compile(Path(_solution.__file__).read_text(), _solution.__file__, "exec"), {})
    return output.getvalue().strip().splitlines()

def test_first_line():
    """Print the reading circle announcement first"""
    lines = _output()
    assert len(lines) >= 1 and lines[0] == "Reading circle starts today", "Print the first announcement line"

def test_second_line():
    """Print the bring-a-book reminder second"""
    lines = _output()
    assert len(lines) >= 2 and lines[1] == "Bring a book", "Add a second print call below the first"
