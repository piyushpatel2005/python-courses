from solution import *


def test_01_resume_parent() -> None:
    first = iter(["a"]); last = iter([])
    frames = [first, last]
    finish_frame(frames)
    assert frames == [first]
    finish_frame(frames)
    assert frames == []


def test_02_remember_neighbor() -> None:
    seen = {"old"}
    remember_neighbor(seen, "new")
    assert seen == {"old", "new"}
    remember_neighbor(seen, "new")
    assert seen == {"old", "new"}


def test_03_record_neighbor() -> None:
    import solution
    # Supply earlier collaborators; grade only this checkpoint.
    original_remember_neighbor = solution.remember_neighbor
    try:
        solution.remember_neighbor = lambda seen, neighbor: seen.add(neighbor)
        assert dfs_iterative({"s": ["a", "a"], "a": []}, "s") == ["s", "a"]
    finally:
        solution.remember_neighbor = original_remember_neighbor


def test_04_descend_frames() -> None:
    import solution
    original_finish = solution.finish_frame
    original_remember = solution.remember_neighbor
    opened: list[str] = []
    class ObservedGraph(dict):
        def __getitem__(self, key: str) -> list[str]:
            opened.append(key)
            return super().__getitem__(key)
    g = ObservedGraph({"s": ["a", "b"], "a": ["b", "c"], "b": ["d"], "c": [], "d": ["s"]})
    try:
        solution.finish_frame = lambda frames: frames.pop()
        solution.remember_neighbor = lambda seen, neighbor: seen.add(neighbor)
        dfs_iterative(g, "s")
        assert opened == ["s", "a", "b", "d", "c"]
        opened.clear()
        chain = ObservedGraph({str(i): [str(i + 1)] for i in range(1200)})
        chain["1200"] = []
        dfs_iterative(chain, "0")
        assert opened == [str(i) for i in range(1201)]
    finally:
        solution.finish_frame = original_finish
        solution.remember_neighbor = original_remember

