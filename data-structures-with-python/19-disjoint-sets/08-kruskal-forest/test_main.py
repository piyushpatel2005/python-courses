from solution import *


def test_stable_weight_order():
    edges = [(0, 1, 4), (2, 3, -1), (1, 2, 4)]
    assert ordered_edges(edges) == [(2, 3, -1), (0, 1, 4), (1, 2, 4)]
    assert edges == [(0, 1, 4), (2, 3, -1), (1, 2, 4)]
    assert ordered_edges([]) == []


def test_accept_only_connecting_edges():
    d = DisjointSet(6)
    edges = [(4, 4, -9), (3, 4, -1), (1, 2, 2), (0, 2, 4), (0, 1, 7)]
    assert choose_forest_edges(d, edges) == [(3, 4, -1), (1, 2, 2), (0, 2, 4)]
    assert d.component_count() == 3
    assert choose_forest_edges(DisjointSet(0), []) == []


def test_total_accepted_weights():
    assert forest_weight([]) == 0
    assert forest_weight([(0, 1, -3), (2, 3, 0), (1, 2, 8)]) == 5
