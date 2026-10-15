from solution import *


def test_01_missing_vertex() -> None:
    g = Graph(["a"])
    assert g.remove_vertex("x") is False
    assert g.adj == {"a": []}


def test_02_incident_edges() -> None:
    g = Graph(["h", "a", "b", "c"])
    for v in ["a", "b", "c"]: g.add_edge("h", v)
    g.add_edge("a", "b")
    g.remove_vertex("h")
    assert g.adj["a"] == ["b"] and g.adj["b"] == ["a"] and g.adj["c"] == []


def test_03_delete_key() -> None:
    g = Graph(["alone"])
    assert g.remove_vertex("alone") is True
    assert g.adj == {}

