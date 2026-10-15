from solution import *


def test_enum_truth_values():
    for member, expected in [(ScreenShake.OFF, False), (ScreenShake.LOW, True), (ScreenShake.HIGH, True)]:
        assert bool(member) is expected
        assert member.__bool__() is expected
