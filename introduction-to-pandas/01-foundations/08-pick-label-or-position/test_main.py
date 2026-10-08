from solution import *
import pandas as pd

def test_01_pick_label_or_position():
    """Select the first position regardless of labels or values."""
    assert chosen == first_count(card) == 7
    for values, labels in [([31, 7, 14], [20, 10, 30]), ([99, -1, 18], [10, 20, 0]), ([42, 3, 18], ["first", "other", "first"])]:
        sample = pd.Series(values, index=labels)
        assert first_count(sample) == sample.iloc[0]

