from solution import *


def test_01_first_parent() -> None:
    g = {"s": ["b", "a"], "a": ["t"], "b": ["t"], "t": []}
    assert bfs_parents(g, "s") == {"s": None, "b": "s", "a": "s", "t": "b"}


def test_02_walk_parents() -> None:
    assert backward_chain({"x": None, "y": "x", "z": "y"}, "z") == ["z", "y", "x"]
    assert backward_chain({"": None}, "") == [""]


def test_03_forward_path() -> None:
    import solution
    # Supply earlier collaborators; grade only this checkpoint.
    def supplied_parents(adj: dict[str, list[str]], start: str) -> dict[str, str | None]:
        return {"s": None, "b": "s", "a": "s", "t": "b"}
    def supplied_chain(parents: dict[str, str | None], target: str) -> list[str]:
        return {"s": ["s"], "t": ["t", "b", "s"]}[target].copy()
    original_bfs_parents = solution.bfs_parents
    original_backward_chain = solution.backward_chain
    try:
        solution.bfs_parents = supplied_parents
        solution.backward_chain = supplied_chain
        g = {"s": ["b", "a"], "a": ["t"], "b": ["t"], "t": [], "idle": []}
        assert bfs_path(g, "s", "t") == ["s", "b", "t"]
        assert bfs_path(g, "s", "s") == ["s"]
        assert bfs_path(g, "s", "idle") == []
    finally:
        solution.bfs_parents = original_bfs_parents
        solution.backward_chain = original_backward_chain

