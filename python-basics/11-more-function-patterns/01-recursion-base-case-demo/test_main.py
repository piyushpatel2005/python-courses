from solution import days_left, sample


def test_sample_countdown():
    """The opening-day countdown stops at zero."""
    assert sample == [3, 2, 1, 0]
    assert days_left(0) == [0]
