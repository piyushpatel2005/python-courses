from solution import *


def test_descriptor_backed_record():
    a, b = CharacterStats(12, 3), CharacterStats(20, 5)
    assert (a.max_health, a.max_mana, b.max_health, b.max_mana) == (12, 3, 20, 5)
    a.max_mana = 4.5
    assert a.max_mana == 4.5 and b.max_mana == 5
    for max_health, max_mana, error in [(0, 2, ValueError), (3, -1, ValueError), (True, 2, TypeError), (3, "2", TypeError)]:
        try:
            CharacterStats(max_health, max_mana)
        except error:
            pass
        else:
            assert False, "Construction must use descriptor validation"
    # A substituted descriptor verifies the taught public assignment route.
    original = CharacterStats.__dict__["max_health"]
    seen = []
    class Spy(Positive):
        def __set__(self, instance, value):
            seen.append(value)
            super().__set__(instance, value)
    replacement = Spy()
    replacement.__set_name__(CharacterStats, "max_health")
    try:
        CharacterStats.max_health = replacement
        obj = CharacterStats(8, 2)
        assert seen == [8] and obj.max_health == 8
    finally:
        CharacterStats.max_health = original
