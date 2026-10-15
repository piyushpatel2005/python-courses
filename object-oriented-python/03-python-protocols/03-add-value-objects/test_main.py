from solution import *


def test_01_add_value_objects():
    for a, b in ((4, 8), (0, 3), (2.5, 1.25)):
        left, right = MovementOffset(a), MovementOffset(b)
        result = left + right
        assert isinstance(result, MovementOffset), "Addition must return a MovementOffset."
        assert result.steps == a + b
        assert result is not left and result is not right
        assert (left.steps, right.steps) == (a, b)
    assert MovementOffset(2).__add__(3) is NotImplemented
    try:
        MovementOffset(2) + 3
    except TypeError:
        pass
    else:
        assert False, "Unsupported addition should let Python raise TypeError."
