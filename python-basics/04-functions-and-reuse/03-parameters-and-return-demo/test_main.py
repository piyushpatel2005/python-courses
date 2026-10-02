from solution import *

def test_ticket_argument():
    """The call passes the new energy"""
    assert boost_energy(12) == 14
    import io
    from contextlib import redirect_stdout
    out = io.StringIO()
    # Imported code runs once; verify the actual supplied call from source.
    import inspect
    assert "boost_energy(12)" in inspect.getsource(__import__("solution"))
