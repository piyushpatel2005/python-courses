from solution import *


def test_01_order_value_objects():
    for values in ((9, 2, 5), (0, 0, -1), (3.5, 1.25, 3)):
        objects = [TrailTime(value) for value in values]
        ordered = sorted(objects)
        assert [item.seconds for item in ordered] == sorted(values)
        assert [item.seconds for item in objects] == list(values)
        assert all(any(item is original for original in objects) for item in ordered)
    assert not TrailTime(4) < TrailTime(4)
    assert TrailTime(3) < TrailTime(5)
    assert TrailTime(1).__lt__(1) is NotImplemented
    try:
        TrailTime(1) < 1
    except TypeError:
        pass
    else:
        assert False, "Unsupported ordering must not invent a result."
