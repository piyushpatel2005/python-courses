from solution import *
import pandas as pd

def test_01_exercise_align_shifts():
    """Make `combine_shifts(first, second)` return their label-aligned sum as a Series."""
    assert isinstance(combine_shifts(pd.Series([3, 5], index=["tea", "jam"]), pd.Series([4, 2], index=["jam", "tea"])), pd.Series) and combine_shifts(pd.Series([3, 5], index=["tea", "jam"]), pd.Series([4, 2], index=["jam", "tea"])).to_dict() == {"tea": 5, "jam": 9} and pd.isna(combine_shifts(pd.Series([3], index=["tea"]), pd.Series([2], index=["jam"])).loc["tea"])

