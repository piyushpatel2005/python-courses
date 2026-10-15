from solution import *


def test_cooldown_setter_validates_before_storing():
    prop = vars(GameItem).get("cooldown_turns")
    assert isinstance(prop, property) and prop.fset is not None, "Add a setter to the cooldown_turns property."
    first, second = GameItem(7), GameItem(2)
    for valid in (1, 14, 3):
        first.cooldown_turns = valid
        assert first.cooldown_turns == valid and second.cooldown_turns == 2
        for invalid in (0, -1, -20):
            try:
                first.cooldown_turns = invalid
            except ValueError:
                pass
            else:
                assert False, "Reject zero and negative cooldowns with ValueError."
            assert first.cooldown_turns == valid, "Validate before overwriting the previous cooldown."
    for invalid in (0, -8):
        try:
            GameItem(invalid)
        except ValueError:
            pass
        else:
            assert False, "Construction must use the same validation rule."
