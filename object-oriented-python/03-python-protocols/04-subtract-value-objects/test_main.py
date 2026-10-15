from solution import *


def test_01_subtract_value_objects():
    for a, b in ((9, 2), (2, 9), (4, 4), (-3, 6)):
        left, right = Offset(a), Offset(b)
        result = left - right
        assert isinstance(result, Offset)
        assert result.steps == a - b, "Keep left-minus-right order."
        assert result is not left and result is not right
        assert (left.steps, right.steps) == (a, b)
    assert Offset(1).__sub__(1) is NotImplemented
    assert Offset(1).__sub__("1") is NotImplemented
