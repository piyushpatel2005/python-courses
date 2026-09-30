from solution import donation_total

def test_donation_total():
    """The result uses both inputs"""
    assert donation_total(8, 3) == 11
    assert donation_total(1, 9) == 10
