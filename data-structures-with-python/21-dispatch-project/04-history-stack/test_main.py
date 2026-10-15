from solution import *


def test_pop_latest_history_id():
    d = DispatchWorkbench({"s": []})
    d.history = ["roof", "gate"]
    assert [d.pop_history(), d.pop_history(), d.pop_history()] == ["gate", "roof", None]


def test_reverse_one_load_contribution():
    d = DispatchWorkbench({"s": []}, days=3)
    d.catalog["x"] = {"day": 1, "units": 4}
    d.loads.add(0, 2)
    d.loads.add(1, 7)
    d.reverse_load("x")
    assert d.loads.range_sum(0, 1) == 2 and d.loads.range_sum(1, 2) == 3


def test_release_without_resubmitting():
    d = DispatchWorkbench({"s": []})
    d.active = {"x", "y"}
    d.release_id("x")
    assert d.active == {"y"} and list(d.pending) == []
