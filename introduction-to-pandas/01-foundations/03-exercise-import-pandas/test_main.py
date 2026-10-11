from solution import *
import pandas as pd

def test_01_count_card():
    """Build a Series from the supplied list, with its default index."""
    for values in [[3, 8], [], [12], [0, 5, 11, 2]]:
        pd.testing.assert_series_equal(count_card(values), pd.Series(values))
