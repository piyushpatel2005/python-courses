from solution import *
import pandas as pd

def test_complete_ratings():
    """Use different fallback values and preserve missing notes"""
    for fallback in [0, 3, 5]:
        frame = pd.DataFrame({"stall": ["A", "B", "C"], "rating": [None, 2, None], "note": [None, "ok", None]}, index=list("xyz"))
        before = frame.copy(deep=True)
        pd.testing.assert_frame_equal(complete_ratings(frame, fallback), frame.fillna({"rating": fallback}))
        pd.testing.assert_frame_equal(frame, before)
