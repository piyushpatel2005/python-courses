from solution import *


def test_01_mark_component() -> None:
    s = {"old"}
    assert collect_component({"a": ["b"], "b": ["a"]}, "a", s) == ["a", "b"]
    assert s == {"old", "a", "b"}


def test_02_all_components() -> None:
    import solution
    # Supply earlier collaborators; grade only this checkpoint.
    def supplied_component(adj: dict[str, list[str]], start: str, seen: set[str]) -> list[str]:
        members = bfs(adj, start)
        seen.update(members)
        return members
    original_collect_component = solution.collect_component
    try:
        solution.collect_component = supplied_component
        g = {"z": ["a"], "a": ["z"], "x": [], "q": ["r"], "r": ["q"]}
        assert components(g) == [["z", "a"], ["x"], ["q", "r"]]
        assert components({}) == []
    finally:
        solution.collect_component = original_collect_component

