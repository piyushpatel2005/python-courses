from solution import *


def test_01_stale_entries() -> None:
    assert stale_entry(9, 5) is True
    assert stale_entry(5, 5) is False
    assert stale_entry(0, 0) is False


def test_02_schedule_improvements() -> None:
    g = {"s": [("a", 9), ("b", 2)], "a": [("t", 1)], "b": [("a", 3), ("t", 10)], "t": [], "idle": []}
    d, p = dijkstra_heap(g, "s")
    assert d == {"s": 0, "a": 5, "b": 2, "t": 6, "idle": inf}
    assert p["a"] == "b" and p["t"] == "a"
    assert d == dijkstra_scan(g, "s")[0]
    assert dijkstra_heap({"s": [("s", 0)]}, "s")[0] == {"s": 0}
    # Equal priorities follow enqueue order, not alphabetic label order.
    ties = {"s": [("z", 1), ("a", 1)], "a": [("t", 1)], "z": [("t", 1)], "t": []}
    assert dijkstra_heap(ties, "s")[1]["t"] == "z"
    # Observe real pushes rather than accepting a substituted scan algorithm.
    import solution
    original_push = solution.heapq.heappush
    pushes: list[tuple[int | float, int, str]] = []
    def observed_push(heap: list[tuple[int | float, int, str]], item: tuple[int | float, int, str]) -> None:
        pushes.append(item)
        original_push(heap, item)
    try:
        solution.heapq.heappush = observed_push
        dijkstra_heap(g, "s")
    finally:
        solution.heapq.heappush = original_push
    assert any(item[0] == 5 and item[2] == "a" for item in pushes)

