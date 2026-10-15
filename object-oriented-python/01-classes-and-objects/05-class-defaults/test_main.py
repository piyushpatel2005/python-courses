from solution import *


def test_items_use_the_class_default():
    assert getattr(GameItem, "cooldown_turns", None) == 7, "Set cooldown_turns in the class body."
    first, second = GameItem(), GameItem()
    assert "cooldown_turns" not in vars(first) and "cooldown_turns" not in vars(second)
    original = GameItem.cooldown_turns
    try:
        GameItem.cooldown_turns = 12
        assert first.cooldown_turns == second.cooldown_turns == GameItem().cooldown_turns == 12, "Instances should consult the shared class default."
    finally:
        GameItem.cooldown_turns = original
