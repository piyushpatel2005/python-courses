from solution import *


def test_claim_only_inactive_id():
    d = DispatchWorkbench({"s": []})
    assert d.claim_id("z") is True and d.claim_id("z") is False
    assert d.claim_id("a") is True and d.active == {"z", "a"}
    assert list(d.pending) == []


def test_append_fifo_pending_ids():
    d = DispatchWorkbench({"s": []})
    d.append_pending("z")
    d.append_pending("a")
    assert list(d.pending) == ["z", "a"]
    assert [d.take_pending(), d.take_pending(), d.take_pending()] == ["z", "a", None]
