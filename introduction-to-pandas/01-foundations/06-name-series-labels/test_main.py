from solution import *
import pandas as pd

def test_01_stall_labels():
    """Label the second count herbs without changing either value."""
    pd.testing.assert_series_equal(stalls, pd.Series([12, 4], index=["fruit", "herbs"]))
