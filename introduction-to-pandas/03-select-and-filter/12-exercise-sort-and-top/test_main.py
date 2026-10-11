from solution import *
import pandas as pd

def test_rank_points():
    """Rank changing pickup tables without changing input"""
    for visits in [[20, 11, 27], [0, 100, -2, 10], [5, 20, 20, 1]]:
        frame = pd.DataFrame({"point": list("ABCD")[:len(visits)], "visits": visits}, index=[f"p{i}" for i in range(len(visits))])
        original = frame.copy(deep=True)
        ranked = rank_points(frame)
        assert ranked["visits"].is_monotonic_decreasing
        pd.testing.assert_frame_equal(ranked.sort_index(), frame.sort_index())
        pd.testing.assert_frame_equal(frame, original)

def test_top_points():
    """Use count, including a tied cutoff, without changing input"""
    frame = pd.DataFrame({"point": list("ABCDE"), "visits": [5, 20, 11, 11, 8]}, index=list("vwxyz"))
    before = frame.copy(deep=True)
    for count in [0, 1, 2, 3, 4, 8]:
        pd.testing.assert_frame_equal(top_points(frame, count), frame.nlargest(count, "visits"))
        pd.testing.assert_frame_equal(frame, before)
