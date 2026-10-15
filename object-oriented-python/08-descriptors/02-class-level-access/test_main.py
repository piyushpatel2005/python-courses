from solution import *


def test_class_level_access():
    descriptor = Record.__dict__["heading"]
    assert Record.heading is descriptor
    assert Record().heading == "Record heading"
    class Child(Record):
        pass
    assert Child.heading is descriptor
    class Other:
        heading = FieldLabel("Other heading")
    assert Other.heading is Other.__dict__["heading"]
    assert Other().heading == "Other heading"
