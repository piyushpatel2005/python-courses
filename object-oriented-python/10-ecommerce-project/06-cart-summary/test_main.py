from solution import *


def test_behavior():
    """Summarize the cart."""
    cart = Cart(Catalog([Product("B", "Brush", 105), Product("A", "Art", 0)]))
    assert cart.summary() == ([], 0)
    cart.add("B", 3)
    cart.add("A", 2)
    expected = ([("A", "Art", 2, 0), ("B", "Brush", 3, 315)], 315)
    assert cart.summary() == expected
    assert cart.summary() == expected
    rows, total = cart.summary()
    rows.clear()
    assert len(cart.lines) == 2
