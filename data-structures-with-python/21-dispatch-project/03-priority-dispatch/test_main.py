from solution import *


def test_make_stable_priority_entry():
    d = DispatchWorkbench({"s": []})
    d.catalog = {"z": {"priority": 2}, "a": {"priority": 2}}
    assert d.priority_entry("z") == (2, 0, "z")
    assert d.priority_entry("a") == (2, 1, "a")
    assert d.sequence == 2 and d.ready == []


def test_pop_next_ready_id():
    from heapq import heapify

    d = DispatchWorkbench({"s": []})
    assert d.take_ready() is None
    d.ready = [(9, 0, "slow"), (1, 1, "z"), (1, 2, "a")]
    heapify(d.ready)
    assert [d.take_ready(), d.take_ready(), d.take_ready(), d.take_ready()] == [
        "z",
        "a",
        "slow",
        None,
    ]
