from solution import *


def test_set_name():
    assert Loadout.weapon.key == "_weapon" and Loadout.armor.key == "_armor"
    a, b = Loadout(), Loadout()
    a.weapon, a.armor, b.weapon = "Bow", "Leather", "Spear"
    assert (a.weapon, a.armor, b.weapon, b.armor) == ("Bow", "Leather", "Spear", None)
    class Other:
        zone = NamedField()
        code = NamedField()
    other = Other()
    other.zone, other.code = 3, "Z"
    assert (other.zone, other.code) == (3, "Z")
    assert Other.zone.key == "_zone"
