from solution import *


def test_01_callable_objects():
    for factor in (0, 3, -2, 1.5):
        multiplier = ScoreMultiplier(factor)
        assert callable(multiplier)
        for value in (0, 7, -4, 2.5):
            assert multiplier(value) == value * factor, "Use this call's value and this instance's factor."
            assert multiplier.factor == factor
    assert ScoreMultiplier(2)(8) != ScoreMultiplier(3)(8)
