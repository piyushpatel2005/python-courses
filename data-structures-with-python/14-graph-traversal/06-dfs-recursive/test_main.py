from solution import *


def test_01_mark_entry() -> None:
    s: set[str] = set(); out: list[str] = []
    dfs_visit({"x": []}, "x", s, out)
    assert s == {"x"}


def test_02_record_entry() -> None:
    out: list[str] = []
    dfs_visit({"x": []}, "x", set(), out)
    assert out == ["x"]


def test_03_depth_first() -> None:
    import solution
    original_visit = solution.dfs_visit
    calls: list[str] = []
    g = {"s": ["b", "a", "b"], "a": [], "b": []}
    seen: set[str] = set()
    order: list[str] = []
    def observe(adj: dict[str, list[str]], vertex: str, supplied_seen: set[str], supplied_order: list[str]) -> None:
        assert adj is g and supplied_seen is seen and supplied_order is order
        calls.append(vertex)
    try:
        solution.dfs_visit = observe
        # Invoke the actual helper once, observing only its recursive dispatch.
        original_visit(g, "s", seen, order)
    finally:
        solution.dfs_visit = original_visit
    assert calls == ["b", "a", "b"]

