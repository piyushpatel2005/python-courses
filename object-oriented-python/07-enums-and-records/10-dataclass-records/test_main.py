from solution import *


def test_dataclass_records():
    from dataclasses import is_dataclass, fields
    assert is_dataclass(PlayerSave)
    assert [(f.name, f.type) for f in fields(PlayerSave)] == [("player_name", str), ("experience", int)]
    a = PlayerSave("Oren")
    b = PlayerSave("Oren")
    assert a.experience == 0 and a == b and a is not b
    a.experience = 17
    assert b.experience == 0 and a != b
    assert PlayerSave("Nia", 9).experience == 9
