from solution import *
import pandas as pd

def test_two_categories():
    """Include fruit and bakery but not craft"""
    pd.testing.assert_frame_equal(result, stalls.loc[stalls["category"].isin(["fruit", "bakery"])])
