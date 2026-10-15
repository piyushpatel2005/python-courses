from solution import *


def test_01_subtract_value_objects():
    for a, b in ((9, 2), (2, 9), (4, 4), (-3, 6)):
        left, right = MovementOffset(a), MovementOffset(b)
        result = left - right
        assert isinstance(result, MovementOffset)
        assert result.steps == a - b, "Keep left-minus-right order."
        assert result is not left and result is not right
        assert (left.steps, right.steps) == (a, b)
    assert MovementOffset(1).__sub__(1) is NotImplemented
    assert MovementOffset(1).__sub__("1") is NotImplemented
