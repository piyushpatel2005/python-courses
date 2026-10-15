from solution import *


def test_01_the_object_base():
    class Plain:
        pass
    class Child(Plain):
        pass
    class Grandchild(Child):
        pass
    assert direct_object_base(Plain()) is True, "Inspect the actual class's direct bases."
    assert direct_object_base(Child()) is False
    assert direct_object_base(Grandchild()) is False
    assert direct_object_base(Record()) is True
    assert direct_object_base(DetailedRecord()) is False
    assert direct_object_base(object()) is False
