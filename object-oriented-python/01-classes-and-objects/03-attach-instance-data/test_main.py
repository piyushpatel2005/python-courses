from solution import *


def test_each_item_keeps_its_name():
    items = [make_item(value) for value in ("lantern", "shield", "", "compass")]
    assert all(isinstance(item, GameItem) for item in items)
    assert [getattr(item, "name", None) for item in items] == ["lantern", "shield", "", "compass"], "Store the name parameter on each item."
    items[0].name = "changed"
    assert items[1].name == "shield", "Names belong to separate instances."
