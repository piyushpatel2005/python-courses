from solution import *

def test_01():
    """Count people once even if they sign in twice."""
    assert type(unique_attendees) is set
    assert unique_attendees == {"Maya", "Luis"}
