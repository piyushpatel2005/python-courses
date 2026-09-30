from solution import *


def test_parse_seats():
    """Valid integers convert; invalid text falls back to zero"""
    assert parse_seats("3") == 3, "Convert digit text with int()."
    assert parse_seats("-2") == -2, "Return the integer value for valid text."
    assert parse_seats("three") == 0, "Catch ValueError and return 0."
    assert parse_seats("") == 0, "Empty text is invalid too."
