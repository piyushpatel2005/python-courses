from solution import *


def test_record_use_updates_its_receiver():
    first, second = make_item(4), make_item(20)
    assert callable(getattr(first, "record_use", None)), "Define record_use inside GameItem with self as its parameter."
    first.record_use()
    first.record_use()
    assert first.uses == 6 and second.uses == 20
    second.record_use()
    assert second.uses == 21 and first.uses == 6, "Use self so each call updates its own receiver."
