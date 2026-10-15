from solution import *


def test_behavior():
    """Name a domain error."""
    assert issubclass(SoldOutError, Exception)
    assert reserve(5) == 4
    assert reserve(1) == 0
    for remaining in (0, -1):
        try:
            reserve(remaining)
        except SoldOutError as error:
            assert str(error) == "workshop is full"
        else:
            assert False, "Raise SoldOutError for a full workshop"
