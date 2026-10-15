from solution import *


def test_01_unknown_start() -> None:
    try:
        bfs({}, "missing")
    except KeyError:
        pass
    else:
        assert False, "Unknown start must raise KeyError"


def test_02_record_start() -> None:
    assert bfs({"solo": []}, "solo") == ["solo"]


def test_03_breadth_first() -> None:
    import solution
    original = solution.discover
    expanded: list[list[str]] = []
    def observe(neighbors: list[str], seen: set[str], frontier: deque[str]) -> None:
        expanded.append(list(neighbors))
        original(neighbors, seen, frontier)
    try:
        solution.discover = observe
        adj = {"s": ["b", "a", "b"], "a": ["s"], "b": ["c"], "c": [], "idle": []}
        bfs(adj, "s")
        assert expanded == [["b", "a", "b"], ["c"], ["s"], []]
        assert adj["s"] == ["b", "a", "b"]
        for length in range(2, 9):
            expanded.clear()
            chain = {str(i): [str(i + 1)] for i in range(length - 1)}
            chain[str(length - 1)] = []
            bfs(chain, "0")
            assert expanded == [[str(i)] for i in range(1, length)] + [[]]
    finally:
        solution.discover = original

