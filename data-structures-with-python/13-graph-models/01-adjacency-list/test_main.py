from solution import *


def test_01_empty_state() -> None:
    a, b = Graph(), Graph()
    assert a.adj == {} and b.adj == {}
    assert a.adj is not b.adj


def test_02_register_labels() -> None:
    labels = ["x", "y", "x"]
    adj: dict[str, list[str]] = {}
    register_vertices(adj, iter(labels))
    assert adj == {"x": [], "y": []}
    assert list(adj) == ["x", "y"]
    adj["x"].append("y")
    register_vertices(adj, ["x", "z"])
    assert adj == {"x": ["y"], "y": [], "z": []}
    assert adj["y"] is not adj["z"]
    labels.append("outside")
    assert "outside" not in adj

