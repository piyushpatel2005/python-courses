from solution import *


def test_available_is_derived_from_current_counts():
    prop = vars(ItemPool).get("available")
    assert isinstance(prop, property) and prop.fset is None, "Define a getter-only property."
    first, second = ItemPool(12, 4), ItemPool(0, 0)
    assert first.available == 8 and second.available == 0
    first.equipped = 9
    assert first.available == 3
    first.total = 15
    assert first.available == 6 and second.available == 0
    second.total = 7
    assert second.available == 7
    assert "available" not in vars(first), "Derive the value instead of storing a second counter."
