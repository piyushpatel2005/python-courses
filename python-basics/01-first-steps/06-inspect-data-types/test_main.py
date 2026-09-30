from solution import *
import solution as _solution

def test_price():
    """Update the decimal price"""
    assert type(price) is float and price == 3.5, "Use 3.5 without quotes"
