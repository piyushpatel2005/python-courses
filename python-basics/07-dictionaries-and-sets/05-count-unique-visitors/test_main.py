from solution import *

def test_01():
    """Set unique to a set of the distinct stops in visited_stops."""
    assert type(unique) is set and unique == {"Ridge", "Cove"}, "Set unique to a set of the distinct stops in visited_stops."
