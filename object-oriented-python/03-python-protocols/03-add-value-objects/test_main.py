from solution import *


def test_01_add_value_objects():
    for a, b in ((4, 8), (0, 3), (2.5, 1.25)):
        left, right = Cable(a), Cable(b)
        result = left + right
        assert isinstance(result, Cable), "Addition must return a Cable."
        assert result.metres == a + b
        assert result is not left and result is not right
        assert (left.metres, right.metres) == (a, b)
    assert Cable(2).__add__(3) is NotImplemented
    try:
        Cable(2) + 3
    except TypeError:
        pass
    else:
        assert False, "Unsupported addition should let Python raise TypeError."
