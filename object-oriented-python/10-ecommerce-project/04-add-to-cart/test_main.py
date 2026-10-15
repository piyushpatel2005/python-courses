from solution import *


def test_behavior():
    """Add products to a cart."""
    catalog = Catalog([Product("X", "Cup", 113), Product("Y", "Tray", 700)])
    cart = Cart(catalog)
    cart.add("X", 2)
    cart.add("X", 3)
    cart.add("Y", 1)
    assert cart.lines["X"].quantity == 5
    assert cart.lines["Y"].subtotal_cents == 700
    assert Cart(catalog).lines == {}
    for quantity in (0, -1, True, 1.5):
        try:
            cart.add("X", quantity)
        except ValueError:
            pass
        else:
            assert False, "Reject invalid quantities"
    assert cart.lines["X"].quantity == 5
    try:
        cart.add("missing", 2)
    except KeyError:
        pass
    else:
        assert False, "Look up the product before adding"
    assert len(cart.lines) == 2
