from solution import *


def test_01_absent_edge() -> None:
    g = Graph(["a", "b"])
    assert g.remove_edge("a", "b") is False
    assert g.remove_edge("missing", "a") is False
    assert g.adj == {"a": [], "b": []}


def test_02_remove_both() -> None:
    g = Graph(["a", "b", "c"])
    g.add_edge("a", "b"); g.add_edge("a", "c")
    assert g.remove_edge("b", "a") is True
    assert g.adj == {"a": ["c"], "b": [], "c": ["a"]}

