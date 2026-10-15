from solution import *


def test_01_endpoints() -> None:
    g = WeightedGraph(["a"])
    for source, target in [("a", "x"), ("x", "a")]:
        try:
            g.add_edge(source, target, 1)
        except KeyError:
            pass
        else:
            assert False
    assert g.adj == {"a": []}


def test_02_valid_weights() -> None:
    g = WeightedGraph(["a", "b"])
    for w in [-1, 1.5, True, float("inf"), float("nan")]:
        try:
            g.add_edge("a", "b", w)
        except ValueError:
            pass
        else:
            assert False, "Reject weights outside the integer contract"
    assert g.adj == {"a": [], "b": []}


def test_03_duplicates() -> None:
    g = WeightedGraph(["a", "b"]); g.adj["a"] = [("b", 4)]
    assert g.add_edge("a", "b", 2) is False
    assert g.adj["a"] == [("b", 4)]


def test_04_weighted_arc() -> None:
    g = WeightedGraph(["a", "b", "idle"])
    assert g.add_edge("a", "b", 0) is True
    assert g.add_edge("a", "a", 3) is True
    assert g.adj == {"a": [("b", 0), ("a", 3)], "b": [], "idle": []}
    assert WeightedGraph(["a"]).adj == {"a": []}

