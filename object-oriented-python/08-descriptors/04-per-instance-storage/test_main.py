from solution import *


def test_per_instance_storage():
    a, b, c = PlayerProfile(), PlayerProfile(), PlayerProfile()
    assert a.badge is None and b.badge is None
    a.badge = "X"
    b.badge = "Y"
    assert a.badge == "X" and b.badge == "Y" and c.badge is None
    a.badge = 42
    assert a.badge == 42 and b.badge == "Y"
    assert a.__dict__[PlayerProfile.badge.key] == 42
    assert b.__dict__[PlayerProfile.badge.key] == "Y"
