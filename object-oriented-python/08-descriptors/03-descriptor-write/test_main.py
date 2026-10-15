from solution import *


def test_descriptor_write():
    first, second = Stock(), Stock()
    for value in [7, 0, 2.5]:
        first.quantity = value
        assert first.quantity == value
        try:
            first.quantity = -3
        except ValueError:
            pass
        else:
            assert False, "Reject negative quantities"
        assert first.quantity == value
    second.quantity = 12
    assert first.quantity == 2.5 and second.quantity == 12
