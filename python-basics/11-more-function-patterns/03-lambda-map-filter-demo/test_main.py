from solution import with_delivery, over_six


def test_delivery_prices():
    """The $2 fee reaches every price before filtering."""
    assert with_delivery == [5, 7, 9]
    assert over_six == [7, 9]
