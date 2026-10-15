from solution import *


def test_property_as_descriptor():
    assert isinstance(Hitbox.area, property)
    a, b = Hitbox(2, 7), Hitbox(5, 0)
    assert a.area == 14 and b.area == 0
    a.width = 9
    assert a.area == 63
    a.__dict__["area"] = -1
    assert a.area == 63
    try:
        a.area = 99
    except AttributeError:
        pass
    else:
        assert False, "Area must stay read-only"
