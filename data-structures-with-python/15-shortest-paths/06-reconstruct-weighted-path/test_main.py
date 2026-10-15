from solution import *


def test_01_backward_links() -> None:
    assert weighted_chain({"a": None, "b": "a", "c": "b"}, "c") == ["c", "b", "a"]
    assert weighted_chain({"": None}, "") == [""]


def test_02_weighted_route() -> None:
    import solution
    # Supply earlier collaborators; grade only this checkpoint.
    def supplied_chain(parents: dict[str, str | None], target: str) -> list[str]:
        return {"a": ["a", "b", "s"], "s": ["s"]}[target].copy()
    original_weighted_chain = solution.weighted_chain
    try:
        solution.weighted_chain = supplied_chain
        g = {"s": [("a", 8), ("b", 2)], "a": [], "b": [("a", 3)], "idle": []}
        d, p = dijkstra_heap(g, "s")
        assert reconstruct_weighted_path(d, p, "a") == ["s", "b", "a"]
        assert reconstruct_weighted_path(d, p, "idle") == []
        assert reconstruct_weighted_path(d, p, "s") == ["s"]
        assert path_cost(g, reconstruct_weighted_path(d, p, "a")) == d["a"]
    finally:
        solution.weighted_chain = original_weighted_chain

