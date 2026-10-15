from solution import *


def test_data_descriptor_priority():
    for number in ["A1", "B9"]:
        badge = Badge(number)
        badge.__dict__["serial"] = "wrong"
        assert badge.serial == number, "Data descriptor must win over instance storage"
        try:
            badge.serial = "replacement"
        except AttributeError:
            pass
        else:
            assert False, "Reject assignment with AttributeError"
        assert badge.serial == number
    assert callable(getattr(type(Badge.__dict__["serial"]), "__set__", None))
