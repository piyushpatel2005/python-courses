from solution import *
import pandas as pd

def test_zero_attendance():
    """Only fill the attendance count"""
    pd.testing.assert_frame_equal(result, sessions.fillna({"attendees": 0}))
