from solution import *


def test_behavior():
    """Carry useful exception details."""
    for requested, available in ((7, 2), (1, 0), (29, 11)):
        error = InventoryShortage(requested, available)
        assert (error.requested, error.available) == (requested, available)
        assert str(error) == f"inventory requested {requested}; available {available}"
        assert error.args == (str(error),)
