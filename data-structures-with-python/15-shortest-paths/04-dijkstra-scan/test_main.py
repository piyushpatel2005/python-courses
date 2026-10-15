from solution import *


def test_01_infinity_entries() -> None:
    d = initial_distances({"a": [], "b": [], "c": []}, "a")
    assert "b" in d and "c" in d
    assert d["b"] == inf and d["c"] == inf
    assert list(d) == ["a", "b", "c"]


def test_02_source_zero() -> None:
    assert initial_distances({"a": []}, "a")["a"] == 0


def test_03_minimum_scan() -> None:
    d = {"first": 4, "later": 4, "near": 2, "far": inf}
    assert smallest_unsettled(d, set()) == "near"
    assert smallest_unsettled(d, {"near"}) == "first"
    assert smallest_unsettled(d, {"near", "first", "later"}) is None
    assert smallest_unsettled({}, set()) is None


def test_04_scan_paths() -> None:
    import solution
    # Supply earlier collaborators; grade only this checkpoint.
    def supplied_distances(adj: dict[str, list[tuple[str, int]]], start: str) -> dict[str, int | float]:
        return {v: 0 if v == start else inf for v in adj}
    def supplied_minimum(distances: dict[str, int | float], settled: set[str]) -> str | None:
        candidates = [v for v in distances if v not in settled and distances[v] != inf]
        return min(candidates, key=distances.get) if candidates else None
    original_initial_distances = solution.initial_distances
    original_smallest_unsettled = solution.smallest_unsettled
    try:
        solution.initial_distances = supplied_distances
        solution.smallest_unsettled = supplied_minimum
        g = {"s": [("a", 9), ("b", 2)], "a": [("t", 1)], "b": [("a", 3), ("t", 10)], "t": [], "idle": []}
        d, p = dijkstra_scan(g, "s")
        assert d == {"s": 0, "a": 5, "b": 2, "t": 6, "idle": inf}
        assert p == {"s": None, "a": "b", "b": "s", "t": "a", "idle": None}
    finally:
        solution.initial_distances = original_initial_distances
        solution.smallest_unsettled = original_smallest_unsettled

