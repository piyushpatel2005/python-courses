from solution import *
import pandas as pd

def test_priority_queue():
    """Priority requires both conditions"""
    for minimum in [4, 2, 6]:
        frame = pd.DataFrame({"request": ["A", "B", "C", "D"], "hours": [4, 2, 6, 1], "urgent": [True, True, False, False]}, index=list("wxyz"))
        pd.testing.assert_frame_equal(priority_queue(frame, minimum), frame.loc[(frame["hours"] >= minimum) & frame["urgent"]])

def test_review_queue():
    """Review admits either condition"""
    for minimum in [4, 2, 7]:
        frame = pd.DataFrame({"request": ["A", "B", "C", "D"], "hours": [4, 2, 6, 1], "urgent": [True, True, False, False]}, index=list("wxyz"))
        pd.testing.assert_frame_equal(review_queue(frame, minimum), frame.loc[(frame["hours"] >= minimum) | frame["urgent"]])
