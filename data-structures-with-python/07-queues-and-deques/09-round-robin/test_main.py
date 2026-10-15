from solution import *



def test_01_step():
    "Complete `validate_jobs` to reject negative, boolean, and noninteger work counts."
    for units in [-1, True, 0.5]:
        try: validate_jobs([("job", units)])
        except ValueError: pass
        else: assert False, "Reject invalid work counts"
    assert validate_jobs([("idle", 0), ("work", 2)]) is None


def test_02_step():
    "Complete `queue_jobs` to enqueue only positive-work pairs in arrival order."
    jobs = [("a", 2), ("idle", 0), ("b", 1)]
    assert list(queue_jobs(jobs)) == [("a", 2), ("b", 1)]
    assert jobs == [("a", 2), ("idle", 0), ("b", 1)]


def test_03_complete_behavior():
    "Complete `round_robin` to service one unit per turn and requeue unfinished jobs."
    jobs = [("a", 3), ("b", 1), ("c", 2), ("idle", 0)]
    saved = jobs[:]
    assert round_robin(jobs) == ["a", "b", "c", "a", "c", "a"]
    assert jobs == saved and round_robin([]) == []
    assert round_robin([("same", 1), ("same", 2)]) == ["same"] * 3
    for units in [-1, True, 1.2]:
        try:
            round_robin([("bad", units)])
        except ValueError:
            pass
        else:
            assert False, "Reject invalid work counts"
