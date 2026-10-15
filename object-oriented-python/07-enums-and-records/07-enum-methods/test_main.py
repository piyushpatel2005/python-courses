from solution import *


def test_enum_methods():
    assert [member.name for member in Shipping] == ["GROUND", "AIR"]
    for member, rate in [(Shipping.GROUND, 3), (Shipping.AIR, 8)]:
        for boxes in [0, 1, 2, 7]:
            assert member.cost(boxes) == rate * boxes
