from solution import *


def test_behavior():
    """Format invoice lines."""
    order = Order("I8", (("Z", "Zip", 3, 9), ("A", "Apron", 2, 2000)), 2009)
    assert Invoice(order).lines() == ["Z | Zip | 3 x | $0.09", "A | Apron | 2 x | $20.00"]
    assert Invoice(Order("E", (), 0)).lines() == []
    assert Invoice(Order("F", (("F", "Free", 1, 0),), 0)).lines() == ["F | Free | 1 x | $0.00"]
