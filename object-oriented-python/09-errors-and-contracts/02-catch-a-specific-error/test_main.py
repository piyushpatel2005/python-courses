from solution import *


def test_behavior():
    """Catch only the expected lookup error."""
    assert locker_label({2: "Mira", 8: "Sol"}, 8) == "Sol"
    assert locker_label({}, 8) == "Unknown locker"
    assert locker_label({1: ""}, 1) == ""
    class Broken:
        def __getitem__(self, key):
            raise RuntimeError("sensor offline")
    try:
        locker_label(Broken(), 3)
    except RuntimeError:
        pass
    else:
        assert False, "Do not catch unrelated exceptions"
