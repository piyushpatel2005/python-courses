from solution import *


def test_enum_truth_values():
    for member, expected in [(Signal.OFF, False), (Signal.LOW, True), (Signal.HIGH, True)]:
        assert bool(member) is expected
        assert member.__bool__() is expected
