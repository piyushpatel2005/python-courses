from solution import *


def test_behavior():
    """Freeze an order snapshot."""
    from dataclasses import FrozenInstanceError
    cart = Cart(Catalog([Product("P", "Pen", 79)]))
    cart.add("P", 3)
    order = snapshot_order("Q7", cart)
    assert order.order_id == "Q7"
    assert order.lines == (("P", "Pen", 3, 237),)
    assert order.total_cents == 237
    cart.add("P", 2)
    cart.remove("P")
    assert order.lines == (("P", "Pen", 3, 237),)
    assert order.total_cents == 237
    try:
        order.total_cents = 0
    except FrozenInstanceError:
        pass
    else:
        assert False, "Keep order data frozen"
    assert snapshot_order("EMPTY", cart).lines == ()
