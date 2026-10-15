from solution import *


def test_01_multiple_inheritance():
    assert InventoryCard.__bases__ == (PrintableCode, TrackableCode), "Use the two bases in the requested order."
    assert "print_label" not in InventoryCard.__dict__
    assert "tracking_path" not in InventoryCard.__dict__
    for code in ("K9", "A-12", "sample"):
        item = InventoryCard(code)
        assert item.code == code
        assert item.print_label() == f"Item {code}"
        assert item.tracking_path() == f"/track/{code}"
        assert isinstance(item, PrintableCode) and isinstance(item, TrackableCode)
