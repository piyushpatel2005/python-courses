from solution import *


def test_behavior():
    """Calculate a cart line."""
    for price, quantity in ((135, 3), (0, 9), (9999, 1)):
        line = CartLine(Product("X", "Item", price), quantity)
        assert line.subtotal_cents == price * quantity
        line.quantity += 1
        assert line.subtotal_cents == price * (quantity + 1)
