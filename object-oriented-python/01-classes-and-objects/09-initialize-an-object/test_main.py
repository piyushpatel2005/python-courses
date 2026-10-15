from solution import *


def test_initialization_stores_each_tools_data():
    first, second = Tool("router", 8), Tool("clamp", 0)
    assert getattr(first, "name", None) == "router" and getattr(first, "uses", None) == 8, "Store both constructor arguments on self."
    assert second.name == "clamp" and second.uses == 0
    first.name, first.uses = "changed", 10
    assert second.name == "clamp" and second.uses == 0
    assert Tool("plane", 37).summary() == "plane: 37 uses"
