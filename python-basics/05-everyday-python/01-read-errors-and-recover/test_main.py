from solution import *


def test_parse_energy():
    """Convert valid energy and recover from invalid text."""
    assert parse_energy("3") == 3, "Convert digit text with int()."
    assert parse_energy("-2") == -2, "Return the integer value for valid text."
    assert parse_energy("unknown") == 0, "Catch ValueError and return 0."
    assert parse_energy("") == 0, "Empty text is invalid too."
