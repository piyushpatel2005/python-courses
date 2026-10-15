from solution import *


def test_one_item_overrides_the_default():
    original = GameItem.cooldown_turns
    try:
        first, second = GameItem(), GameItem()
        set_cooldown(first, 11)
        assert first.cooldown_turns == 11, "Assign the override on the supplied item."
        assert second.cooldown_turns == GameItem.cooldown_turns == original, "Do not change the class default."
        set_cooldown(first, 3)
        assert first.cooldown_turns == 3, "turns is the replacement period, not an increment."
        GameItem.cooldown_turns = 9
        assert first.cooldown_turns == 3 and second.cooldown_turns == 9
    finally:
        GameItem.cooldown_turns = original
