from solution import *


def test_behavior():
    """Checkout without losing the cart."""
    cart = Cart(Catalog([Product("R", "Ribbon", 45)]))
    service = CheckoutService()
    try:
        service.checkout(cart, "A")
    except ValueError as error:
        assert str(error) == "cart is empty"
    else:
        assert False, "Reject empty checkout"
    cart.add("R", 4)
    order = service.checkout(cart, "B")
    assert order.order_id == "B" and order.total_cents == 180
    assert cart.lines == {}
    class BrokenCart:
        def __init__(self):
            self.lines = {"keep": 1}
        def summary(self):
            raise RuntimeError("snapshot failed")
    broken = BrokenCart()
    try:
        service.checkout(broken, "C")
    except RuntimeError:
        pass
    else:
        assert False, "Propagate snapshot failure"
    assert broken.lines == {"keep": 1}
