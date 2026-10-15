from solution import *


def test_01_inherit_a_method():
    assert issubclass(SupplyChest, GameEntity), "Use GameEntity as the base class."
    assert "label" not in SupplyChest.__dict__, "Inherit label rather than duplicate it."
    assert "__init__" not in SupplyChest.__dict__
    for code in ("B7", "N-12", ""):
        item = SupplyChest(code)
        assert isinstance(item, GameEntity)
        assert item.code == code and item.label() == f"GameEntity {code}"
