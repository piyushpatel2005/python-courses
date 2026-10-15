from solution import *


def test_usage_updates_accumulate():
    first, other = make_item(7), make_item(2)
    for amount, expected in ((4, 11), (0, 11), (6, 17)):
        record_uses(first, amount)
        assert first.uses == expected, "Add to the existing count rather than replacing it."
        assert other.uses == 2, "Only update the supplied object."
    record_uses(other, 3)
    assert other.uses == 5 and first.uses == 17
