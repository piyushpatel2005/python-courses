from solution import *
import pandas as pd

def test_invited():
    """Match changing invite lists, including empty matches"""
    frame = pd.DataFrame({"session": ["A", "B", "C", "D"], "type": ["food", "garden", "craft", "food"]}, index=list("abcd"))
    for types in [["food"], ["craft", "garden"], [], ["unknown"]]:
        pd.testing.assert_frame_equal(invited(frame, types), frame.loc[frame["type"].isin(types)])
