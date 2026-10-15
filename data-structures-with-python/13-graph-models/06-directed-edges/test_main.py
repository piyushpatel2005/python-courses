from solution import *


def test_01_missing_endpoint() -> None:
    g = DirectedGraph(["a"])
    for a, b in [("a", "x"), ("x", "a")]:
        try:
            g.add_edge(a, b)
        except KeyError:
            pass
        else:
            assert False, "Reject missing endpoints"
    assert g.adj == {"a": []}


def test_02_self_loop() -> None:
    g = DirectedGraph(["a"])
    try:
        g.add_edge("a", "a")
    except ValueError:
        pass
    else:
        assert False, "Reject self-loops"
    assert g.adj == {"a": []}


def test_03_duplicate() -> None:
    g = DirectedGraph(["a", "b"])
    g.adj = {"a": ["b"], "b": []}
    assert g.add_edge("a", "b") is False
    assert g.adj["a"] == ["b"]


def test_04_insert() -> None:
    g = DirectedGraph(["a", "b", "c"])
    assert g.add_edge("a", "b") is True
    assert g.add_edge("a", "c") is True
    assert g.adj == {"a": ["b", "c"], "b": [], "c": []}

