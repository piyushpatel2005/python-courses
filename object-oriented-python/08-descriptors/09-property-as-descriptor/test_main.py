from solution import *


def test_property_as_descriptor():
    assert isinstance(Rectangle.area, property)
    a, b = Rectangle(2, 7), Rectangle(5, 0)
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
