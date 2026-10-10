from solution import *
import pandas as pd

def test_01_last_count():
    """Change the last count to 7; keep the first two counts."""
    pd.testing.assert_series_equal(counts, pd.Series([4, 6, 7]))
