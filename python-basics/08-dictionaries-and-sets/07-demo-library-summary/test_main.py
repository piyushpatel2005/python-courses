from solution import *

def test_01():
    """Count distinct borrowers while retaining all loans."""
    assert borrowers == 2
    assert book_counts == {"Gardening": 2, "Cooking": 1}
