from solution import *
import pandas as pd

def test_01_exercise_default_index():
    """Return the Series index, not a Series or hardcoded label list."""
    for counts in [[], [9], [6, 2, 5], [1, 4, 8, 10]]:
        actual = arrival_labels(counts)
        assert isinstance(actual, pd.Index)
        pd.testing.assert_index_equal(actual, pd.Series(counts).index)

