from solution import *


def test_descriptor_backed_record():
    a, b = Plant(12, 3), Plant(20, 5)
    assert (a.height, a.water, b.height, b.water) == (12, 3, 20, 5)
    a.water = 4.5
    assert a.water == 4.5 and b.water == 5
    for height, water, error in [(0, 2, ValueError), (3, -1, ValueError), (True, 2, TypeError), (3, "2", TypeError)]:
        try:
            Plant(height, water)
        except error:
            pass
        else:
            assert False, "Construction must use descriptor validation"
    # A substituted descriptor verifies the taught public assignment route.
    original = Plant.__dict__["height"]
    seen = []
    class Spy(Positive):
        def __set__(self, instance, value):
            seen.append(value)
            super().__set__(instance, value)
    replacement = Spy()
    replacement.__set_name__(Plant, "height")
    try:
        Plant.height = replacement
        obj = Plant(8, 2)
        assert seen == [8] and obj.height == 8
    finally:
        Plant.height = original
