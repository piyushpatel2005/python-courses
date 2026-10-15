from solution import *


def test_descriptor_write():
    first, second = ManaPool(), ManaPool()
    for value in [7, 0, 2.5]:
        first.mana = value
        assert first.mana == value
        try:
            first.mana = -3
        except ValueError:
            pass
        else:
            assert False, "Reject negative mana amounts"
        assert first.mana == value
    second.mana = 12
    assert first.mana == 2.5 and second.mana == 12
