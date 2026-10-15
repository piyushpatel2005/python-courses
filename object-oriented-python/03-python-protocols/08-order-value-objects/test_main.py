from solution import *


def test_01_order_value_objects():
    for values in ((9, 2, 5), (0, 0, -1), (3.5, 1.25, 3)):
        objects = [RaceTime(value) for value in values]
        ordered = sorted(objects)
        assert [item.seconds for item in ordered] == sorted(values)
        assert [item.seconds for item in objects] == list(values)
        assert all(any(item is original for original in objects) for item in ordered)
    assert not RaceTime(4) < RaceTime(4)
    assert RaceTime(3) < RaceTime(5)
    assert RaceTime(1).__lt__(1) is NotImplemented
    try:
        RaceTime(1) < 1
    except TypeError:
        pass
    else:
        assert False, "Unsupported ordering must not invent a result."
