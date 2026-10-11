from solution import *
import pandas as pd

def test_01_shift_card():
    """Pair each supplied name with its count, in order."""
    for names, values in [(["east", "west"], [4, 9]), (["solo"], [13]), (["z", "a", "m"], [8, 0, 3]), ([], [])]:
        pd.testing.assert_series_equal(shift_card(names, values), pd.Series(values, index=names))
