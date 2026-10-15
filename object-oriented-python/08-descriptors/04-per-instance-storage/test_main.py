from solution import *


def test_per_instance_storage():
    a, b, c = Locker(), Locker(), Locker()
    assert a.code is None and b.code is None
    a.code = "X"
    b.code = "Y"
    assert a.code == "X" and b.code == "Y" and c.code is None
    a.code = 42
    assert a.code == 42 and b.code == "Y"
    assert a.__dict__[Locker.code.key] == 42
    assert b.__dict__[Locker.code.key] == "Y"
