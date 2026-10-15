from solution import *


def test_reusable_validation():
    a, b = Hitbox(), Hitbox()
    a.width, a.height, b.width, b.height = 2.5, 30, 7, 90
    assert (a.width, a.height, b.width, b.height) == (2.5, 30, 7, 90)
    for field in ["width", "height"]:
        previous = getattr(a, field)
        for value, error in [(0, ValueError), (-1, ValueError), (True, TypeError), (False, TypeError), ("4", TypeError), (None, TypeError)]:
            try:
                setattr(a, field, value)
            except error:
                pass
            else:
                assert False, "Reject invalid values with the specified exception"
            assert getattr(a, field) == previous
        setattr(a, field, 1.25)
        assert getattr(a, field) == 1.25
    assert (b.width, b.height) == (7, 90)
