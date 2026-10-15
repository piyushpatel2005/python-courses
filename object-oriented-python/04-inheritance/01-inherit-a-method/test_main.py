from solution import *


def test_01_inherit_a_method():
    assert issubclass(ColdLocker, Locker), "Use Locker as the base class."
    assert "label" not in ColdLocker.__dict__, "Inherit label rather than duplicate it."
    assert "__init__" not in ColdLocker.__dict__
    for code in ("B7", "N-12", ""):
        item = ColdLocker(code)
        assert isinstance(item, Locker)
        assert item.code == code and item.label() == f"Locker {code}"
