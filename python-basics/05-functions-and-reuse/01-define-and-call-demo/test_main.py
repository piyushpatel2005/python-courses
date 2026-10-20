from solution import welcome
import io
from contextlib import redirect_stdout

def test_welcome_message():
    """Calling welcome prints the afternoon greeting."""
    out = io.StringIO()
    with redirect_stdout(out): welcome()
    assert out.getvalue().strip() == "Welcome to the afternoon workshop"
