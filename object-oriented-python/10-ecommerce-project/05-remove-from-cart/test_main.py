from solution import *


def test_behavior():
    """Remove a cart line."""
    cart = Cart(Catalog([Product("A", "A", 20), Product("B", "B", 30)]))
    cart.add("A", 4)
    cart.add("B", 2)
    assert cart.remove("A") is True
    assert "A" not in cart.lines
    assert cart.lines["B"].quantity == 2
    assert cart.remove("A") is False
    assert cart.remove("B") is True
    assert cart.lines == {}
    assert cart.remove("missing") is False
