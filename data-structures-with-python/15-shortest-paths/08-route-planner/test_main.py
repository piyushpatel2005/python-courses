from solution import *


def test_01_one_report() -> None:
    d = {"s": 0, "t": 4, "idle": inf}; p = {"s": None, "t": "s", "idle": None}
    assert route_report(d, p, "t") == {"target": "t", "cost": 4, "path": ["s", "t"]}
    assert route_report(d, p, "idle") == {"target": "idle", "cost": None, "path": []}


def test_02_batch_routes() -> None:
    import solution
    # Supply earlier collaborators; grade only this checkpoint.
    def supplied_report(distances: dict[str, int | float], parents: dict[str, str | None], target: str) -> dict[str, object]:
        return {"target": target, "cost": None if distances[target] == inf else distances[target], "path": reconstruct_weighted_path(distances, parents, target)}
    original_route_report = solution.route_report
    try:
        solution.route_report = supplied_report
        g = {"s": [("a", 6), ("b", 1)], "a": [], "b": [("a", 2)], "idle": []}
        rows = plan_routes(g, "s", ["a", "idle", "s", "a"])
        assert rows == [{"target": "a", "cost": 3, "path": ["s", "b", "a"]}, {"target": "idle", "cost": None, "path": []}, {"target": "s", "cost": 0, "path": ["s"]}, {"target": "a", "cost": 3, "path": ["s", "b", "a"]}]
        rows[0]["path"].append("changed")
        assert rows[3]["path"] == ["s", "b", "a"]
        assert plan_routes(g, "s", []) == []
        assert g["s"] == [("a", 6), ("b", 1)]
        import solution
        original_search = solution.dijkstra_heap
        calls: list[str] = []
        def counted_search(adj: dict[str, list[tuple[str, int]]], start: str) -> tuple[dict[str, int | float], dict[str, str | None]]:
            calls.append(start)
            return original_search(adj, start)
        try:
            solution.dijkstra_heap = counted_search
            plan_routes(g, "s", ["a", "b", "a"])
        finally:
            solution.dijkstra_heap = original_search
        assert calls == ["s"]
    finally:
        solution.route_report = original_route_report

