from solution import *


def test_class_level_access():
    descriptor = PlayerSave.__dict__["heading"]
    assert PlayerSave.heading is descriptor
    assert PlayerSave().heading == "Player save"
    class Child(PlayerSave):
        pass
    assert Child.heading is descriptor
    class Other:
        heading = FieldLabel("Other heading")
    assert Other.heading is Other.__dict__["heading"]
    assert Other().heading == "Other heading"
