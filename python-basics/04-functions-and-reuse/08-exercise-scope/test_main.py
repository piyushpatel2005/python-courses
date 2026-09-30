from solution import sale_price, price

def test_local_price():
    """The discount is local"""
    assert sale_price() == 15
    assert price == 20
