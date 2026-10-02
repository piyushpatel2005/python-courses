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
    """Print the lantern map prompt first"""
    lines = _output()
    assert len(lines) >= 1 and lines[0] == "The lantern map is open", "Print the first map line"

def test_second_line():
    """Print the beacon reminder second"""
    lines = _output()
    assert len(lines) >= 2 and lines[1] == "Find the first beacon", "Add a second print call below the first"
