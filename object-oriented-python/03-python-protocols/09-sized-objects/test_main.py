from solution import *


def test_01_sized_objects():
    for items in ([], ["A"], ["A", "B", "C", "D"]):
        inventory = Inventory(items)
        assert len(inventory) == len(items), "Count the current contained list."
        inventory.items.append("new")
        assert len(inventory) == len(items) + 1
        inventory.items.clear()
        assert len(inventory) == 0
    assert not Inventory([])
    assert bool(Inventory(["potion"]))
