from solution import *


def test_dataclass_records():
    from dataclasses import is_dataclass, fields
    assert is_dataclass(Reading)
    assert [(f.name, f.type) for f in fields(Reading)] == [("title", str), ("pages", int)]
    a = Reading("Field notes")
    b = Reading("Field notes")
    assert a.pages == 0 and a == b and a is not b
    a.pages = 17
    assert b.pages == 0 and a != b
    assert Reading("Maps", 9).pages == 9
