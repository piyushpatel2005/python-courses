from solution import with_fee, over_six

def test_price_fee():
    assert with_fee == [5, 7, 9]
    assert over_six == [7, 9]
