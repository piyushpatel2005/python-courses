from solution import *


def test_01_custom_format():
    for metres in (0, 18, 2.5):
        distance = Distance(metres)
        assert format(distance) == f"{metres} m"
        assert format(distance, "short") == f"{metres} m"
        assert f"{distance:long}" == f"{metres} metres"
        assert distance.metres == metres
        for bad in ("wide", "LONG", ".2f"):
            try:
                format(distance, bad)
            except ValueError as error:
                assert str(error), "Give a useful invalid-format message."
            else:
                assert False, "Unknown format specifications must raise ValueError."
