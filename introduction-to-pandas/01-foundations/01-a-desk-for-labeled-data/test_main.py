from solution import *
import pandas as pd

def test_01_bread_count():
    """Change bread to 11 and keep flowers at 5."""
    pd.testing.assert_series_equal(counts, pd.Series([11, 5], index=["bread", "flowers"]))
