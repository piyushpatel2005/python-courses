from solution import *


def test_reachable_distance_including_zero():
    distance = {"a": 0, "b": 7, "x": float("inf")}
    assert DispatchWorkbench.route_exists(distance, "a") is True
    assert DispatchWorkbench.route_exists(distance, "b") is True
    assert DispatchWorkbench.route_exists(distance, "x") is False


def test_rebuild_forward_weighted_path():
    previous = {"store": "depot", "yard": "store"}
    assert DispatchWorkbench.rebuild_path(previous, "depot", "yard") == [
        "depot",
        "store",
        "yard",
    ]
    assert DispatchWorkbench.rebuild_path({}, "depot", "depot") == ["depot"]
    assert previous == {"store": "depot", "yard": "store"}
