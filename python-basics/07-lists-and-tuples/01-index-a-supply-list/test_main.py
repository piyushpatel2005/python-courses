from solution import *

def test_01():
    """Read the last item, not the first."""
    assert last_item == groceries[-1] == "apples"
