from solution import *


def test_01_truthy_objects():
    for charge, enabled, expected in ((8, True, True), (0, True, False), (-2, True, False), (8, False, False), (0.5, True, True)):
        battery = Battery(charge, enabled)
        assert battery.__bool__() is expected, "Return a bool for the complete usability rule."
        assert bool(battery) is expected
    battery = Battery(3)
    battery.enabled = False
    assert not battery
    battery.enabled = True
    battery.charge = 0
    assert not battery
