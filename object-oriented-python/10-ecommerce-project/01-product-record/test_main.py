from solution import *


def test_behavior():
    """Validate a product record."""
    from dataclasses import FrozenInstanceError
    for price in (0, 1, 1299):
        p = Product("T", "Tin", price)
        assert p.price_cents == price
    for args in (("", "Tin", 1), ("T", " ", 1), (None, "Tin", 1), ("T", "Tin", -1), ("T", "Tin", True), ("T", "Tin", 1.2)):
        try:
            Product(*args)
        except ValueError:
            pass
        else:
            assert False, "Reject invalid product data"
    try:
        p.name = "changed"
    except FrozenInstanceError:
        pass
    else:
        assert False, "Product records are frozen"
