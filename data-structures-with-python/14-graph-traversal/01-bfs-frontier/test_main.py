from solution import *


def test_01_remember_discovery() -> None:
    s = {"old"}; q = deque()
    discover(["old", "new", "new", "other"], s, q)
    assert s == {"old", "new", "other"}


def test_02_enqueue_once() -> None:
    # Discovery-set mutation has its own checkpoint; use distinct new labels here.
    s = {"old"}
    q = deque(["waiting"])
    discover(["new", "old", "other"], s, q)
    assert list(q) == ["waiting", "new", "other"]
    discover(["old"], s, q)
    assert list(q) == ["waiting", "new", "other"]

