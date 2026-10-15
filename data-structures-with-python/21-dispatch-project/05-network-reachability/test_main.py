from solution import *


def test_validate_both_network_sites():
    d = DispatchWorkbench({"a": [], "b": []})
    assert d.check_sites("a", "b") is None
    for pair in [("missing", "a"), ("a", "missing"), ("missing", "missing")]:
        try:
            d.check_sites(*pair)
        except KeyError:
            pass
        else:
            assert False


def test_queue_each_unseen_neighbor_once():
    from collections import deque

    d = DispatchWorkbench({"a": [("a", 0), ("b", 2), ("c", 1)], "b": [], "c": []})
    seen = {"a"}
    frontier = deque(["old"])
    d.queue_unseen("a", seen, frontier)
    assert list(frontier) == ["old", "b", "c"] and seen == {"a", "b", "c"}
    d.queue_unseen("a", seen, frontier)
    assert list(frontier) == ["old", "b", "c"]
