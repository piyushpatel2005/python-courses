from solution import *


def test_descriptor_read():
    assert isinstance(CharacterStats.__dict__["power"], ScaledPower)
    assert CharacterStats.power is CharacterStats.__dict__["power"]
    for base_power in [0, 3, -2, 11]:
        character = CharacterStats(base_power)
        assert character.power == base_power * 10
        character.base_power = base_power + 1
        assert character.power == (base_power + 1) * 10
