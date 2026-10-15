from solution import *


def test_01_slots_in_subclasses():
    slots = vars(NamedWaypoint).get("__slots__", ())
    names = (slots,) if isinstance(slots, str) else tuple(slots)
    assert names == ("label",), "Declare only the new field."
    for x, y, label in ((4, 7, "gate"), (0, -2, "origin")):
        point = NamedWaypoint(x, y, label)
        assert (point.x, point.y, point.label) == (x, y, label)
        assert not hasattr(point, "__dict__")
        point.x, point.y, point.label = y, x, "changed"
        assert (point.x, point.y, point.label) == (y, x, "changed")
        try:
            point.extra = 1
        except AttributeError:
            pass
        else:
            assert False, "The subclass must not regain arbitrary fields."
