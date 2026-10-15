from solution import *


def test_initialization_stores_each_items_data():
    first, second = GameItem("bow", 8), GameItem("compass", 0)
    assert getattr(first, "name", None) == "bow" and getattr(first, "uses", None) == 8, "Store both constructor arguments on self."
    assert second.name == "compass" and second.uses == 0
    first.name, first.uses = "changed", 10
    assert second.name == "compass" and second.uses == 0
    assert GameItem("horn", 37).summary() == "horn: 37 uses"
