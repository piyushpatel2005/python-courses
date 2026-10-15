from solution import *


def test_enum_methods():
    assert [member.name for member in Ability] == ["DASH", "HEAL"]
    for member, rate in [(Ability.DASH, 3), (Ability.HEAL, 8)]:
        for casts in [0, 1, 2, 7]:
            assert member.cost(casts) == rate * casts
