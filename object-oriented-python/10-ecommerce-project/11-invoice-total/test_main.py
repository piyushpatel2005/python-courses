from solution import *


def test_behavior():
    """Render the complete invoice."""
    invoice = Invoice(Order("K9", (("P", "Pin", 2, 102),), 102))
    assert invoice.render() == "Order K9\nP | Pin | 2 x | $1.02\nTotal: $1.02"
    assert Invoice(Order("EMPTY", (), 0)).render() == "Order EMPTY\nTotal: $0.00"
    assert not invoice.render().endswith("\n")
