from solution import tuned, strong

def test_tuned_frequencies():
    """The new adjustment reaches each frequency"""
    assert tuned == [5, 7, 9]
    assert strong == [7, 9]
