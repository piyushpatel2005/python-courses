from solution import *

def test_01():
    """Set unique to a set of the distinct names in visitors."""
    assert type(unique) is set and unique == {"Mara", "Noel"}, "Set unique to a set of the distinct names in visitors."
