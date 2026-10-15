from solution import *


def test_01_truthy_objects():
    for points, enabled, expected in ((8, True, True), (0, True, False), (-2, True, False), (8, False, False), (0.5, True, True)):
        stamina = Stamina(points, enabled)
        assert stamina.__bool__() is expected, "Return a bool for the complete usability rule."
        assert bool(stamina) is expected
    stamina = Stamina(3)
    stamina.enabled = False
    assert not stamina
    stamina.enabled = True
    stamina.points = 0
    assert not stamina
