from solution import *


def test_01_callable_objects():
    for factor in (0, 3, -2, 1.5):
        scaler = Scaler(factor)
        assert callable(scaler)
        for value in (0, 7, -4, 2.5):
            assert scaler(value) == value * factor, "Use this call's value and this instance's factor."
            assert scaler.factor == factor
    assert Scaler(2)(8) != Scaler(3)(8)
