from solution import *


def test_behavior():
    """Register and track an order."""
    registry = OrderRegistry()
    a = Order("A", (("X", "X", 1, 20),), 20)
    b = Order("B", (), 0)
    registry.add(a)
    registry.add(b)
    assert registry.get("A") is a
    assert registry.track("A") == "placed"
    registry.advance("A", "shipped")
    try:
        registry.add(Order("A", (), 0))
    except ValueError:
        pass
    else:
        assert False, "Reject duplicate IDs"
    assert registry.get("A") is a
    assert registry.track("A") == "shipped"
    assert registry.track("B") == "placed"
    assert OrderRegistry().orders == {}
