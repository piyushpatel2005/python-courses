from solution import *
import pandas as pd

def test_01_combine_shifts():
    """Add matching labels and leave unmatched totals missing."""
    pairs = [
        (pd.Series([3, 5], index=["tea", "jam"]), pd.Series([4, 2], index=["jam", "tea"])),
        (pd.Series([8, 1], index=["a", "b"]), pd.Series([9, 4], index=["b", "a"])),
        (pd.Series([3, 8], index=["tea", "jam"]), pd.Series([2, 4], index=["jam", "bread"])),
    ]
    for first, second in pairs:
        pd.testing.assert_series_equal(combine_shifts(first, second), first + second)
