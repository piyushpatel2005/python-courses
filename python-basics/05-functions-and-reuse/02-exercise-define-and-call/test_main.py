from solution import announce
import io
from contextlib import redirect_stdout

def test_announce():
    """The announcement runs when called"""
    out = io.StringIO()
    with redirect_stdout(out): announce()
    assert out.getvalue().strip() == "Beacon restored"
