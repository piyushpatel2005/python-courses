from solution import *


def test_01_incoming_counts() -> None:
    assert initial_indegrees({"a": ["c", "c"], "b": ["c"], "c": [], "idle": []}) == {"a": 0, "b": 0, "c": 3, "idle": 0}


def test_02_release_dependencies() -> None:
    import solution
    # Supply earlier collaborators; grade only this checkpoint.
    def supplied_counts(adj: dict[str, list[str]]) -> dict[str, int]:
        return {v: sum(neighbors.count(v) for neighbors in adj.values()) for v in adj}
    original_initial_indegrees = solution.initial_indegrees
    try:
        solution.initial_indegrees = supplied_counts
        g = {"t": ["end"], "b": ["t"], "a": ["t"], "end": []}
        assert topological_order(g) == ["b", "a", "t", "end"]
        assert topological_order({"s": ["t", "t"], "t": []}) == ["s", "t"]
    finally:
        solution.initial_indegrees = original_initial_indegrees


def test_03_reject_cycle() -> None:
    import solution
    # Supply earlier collaborators; grade only this checkpoint.
    def supplied_counts(adj: dict[str, list[str]]) -> dict[str, int]:
        return {v: sum(neighbors.count(v) for neighbors in adj.values()) for v in adj}
    original_initial_indegrees = solution.initial_indegrees
    try:
        solution.initial_indegrees = supplied_counts
        for g in [{"a": ["b"], "b": ["a"]}, {"idle": [], "loop": ["loop"]}]:
            try:
                topological_order(g)
            except ValueError:
                pass
            else:
                assert False, "Cycles have no topological ordering"
        assert topological_order({}) == []
    finally:
        solution.initial_indegrees = original_initial_indegrees

