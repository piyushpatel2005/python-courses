from solution import *


def test_01_existing_vertex() -> None:
    g = Graph(["a", "b"]); g.adj["a"].append("b")
    assert g.add_vertex("a") is False
    assert g.adj["a"] == ["b"]


def test_02_new_vertex() -> None:
    g = Graph(["a"])
    assert g.add_vertex("b") is True
    assert g.adj == {"a": [], "b": []}
    assert g.adj["a"] is not g.adj["b"]
    assert Graph().add_vertex("") is True

