from solution import *


def test_default_and_explicit_usage_counts():
    new = GameItem("new lantern")
    assert new.uses == 0 and new.name == "new lantern", "An omitted uses argument should default to zero."
    assert GameItem("shield", 12).uses == 12
    assert GameItem(name="horn", uses=5).uses == 5
    new.uses = 99
    assert GameItem("another").uses == 0, "Each new item starts with its own count."
