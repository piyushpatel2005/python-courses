from solution import *


def test_item_is_a_class():
    assert "GameItem" in globals(), "Define the GameItem class above the console probe."
    assert isinstance(GameItem, type), "GameItem must be a class, not an instance or a function."
    first, second = GameItem(), GameItem()
    assert isinstance(first, GameItem) and isinstance(second, GameItem)
    assert first is not second, "Calling GameItem twice should create separate instances."
