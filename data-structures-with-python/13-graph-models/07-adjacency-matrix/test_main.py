from solution import *


def test_01_labels() -> None:
    assert adjacency_matrix({"z": [], "a": []})[0] == ["z", "a"]


def test_02_independent_rows() -> None:
    m = zero_matrix(["a", "b"])
    assert m == [[0, 0], [0, 0]]
    m[0][0] = 9
    assert m[1][0] == 0
    assert zero_matrix([]) == []
    assert zero_matrix(["one"]) == [[0]]


def test_03_edge_cells() -> None:
    a = {"z": ["a", "a"], "a": ["a"]}
    m = [[0, 0], [0, 0]]
    fill_matrix(a, {"z": 0, "a": 1}, m)
    assert m == [[0, 1], [0, 1]]
    assert a == {"z": ["a", "a"], "a": ["a"]}
    fill_matrix({}, {}, [])

