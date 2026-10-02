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

def test_greeting():
    """Print the new welcome message"""
    assert _output() == ["Ari enters Spawn Camp"], "Change the text inside print's quotes"
