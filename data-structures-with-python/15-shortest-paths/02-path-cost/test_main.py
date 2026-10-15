from solution import *


def test_01_find_weight() -> None:
    g = {"a": [("b", 0), ("c", 9)], "b": [], "c": []}
    assert edge_weight(g, "a", "b") == 0
    assert edge_weight(g, "a", "c") == 9
    try:
        edge_weight(g, "b", "a")
    except KeyError:
        pass
    else:
        assert False


def test_02_sum_route() -> None:
    import solution
    # Supply earlier collaborators; grade only this checkpoint.
    original_edge_weight = solution.edge_weight
    try:
        solution.edge_weight = lambda adj, source, target: dict(adj[source])[target]
        g = {"a": [("b", 4), ("c", 1)], "b": [("c", 3)], "c": []}
        assert path_cost(g, ["a", "b", "c"]) == 7
        assert path_cost(g, ["a", "c"]) == 1
        assert path_cost(g, []) == 0 and path_cost(g, ["b"]) == 0
        try:
            path_cost(g, ["c", "a"])
        except KeyError:
            pass
        else:
            assert False
    finally:
        solution.edge_weight = original_edge_weight

