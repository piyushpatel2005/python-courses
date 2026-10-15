from solution import *


def test_01_ignore_parent() -> None:
    assert not undirected_back_edge("p", "p", {"p", "q"})
    assert undirected_back_edge("q", "p", {"p", "q"})
    assert not undirected_back_edge("new", "p", {"p"})


def test_02_cycle_anywhere() -> None:
    import solution
    # Supply earlier collaborators; grade only this checkpoint.
    original_undirected_back_edge = solution.undirected_back_edge
    try:
        solution.undirected_back_edge = lambda neighbor, parent, seen: neighbor in seen and neighbor != parent
        assert not undirected_cycle({"a": ["b"], "b": ["a"]})
        assert undirected_cycle({"idle": [], "a": ["b", "c"], "b": ["a", "c"], "c": ["a", "b"]})
        assert not undirected_cycle({})
        assert undirected_cycle({"loop": ["loop"]})
    finally:
        solution.undirected_back_edge = original_undirected_back_edge

