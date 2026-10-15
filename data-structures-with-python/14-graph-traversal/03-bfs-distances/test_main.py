from solution import *


def test_01_zero_at_start() -> None:
    assert bfs_distances({"s": []}, "s") == {"s": 0}


def test_02_shortest_hops() -> None:
    for distance in [0, 1, 5, 11]:
        distances = {"from": distance, "other": 9}
        record_hop(distances, "from", "to")
        assert distances == {"from": distance, "other": 9, "to": distance + 1}

