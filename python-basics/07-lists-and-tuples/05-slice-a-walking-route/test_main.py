from solution import *

def test_01():
    """Slice the first two addresses without changing the list."""
    assert next_addresses == ["Oak Street", "Main Street"]
    assert addresses == ["Oak Street", "Main Street", "Hill Road"]
