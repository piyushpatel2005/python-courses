from solution import *
import pandas as pd

def test_01_name_series_labels():
    """Replace the index label `unknown` with `herbs`."""
    assert isinstance(stalls, pd.Series) and stalls.index.tolist() == ["fruit", "herbs"] and stalls.tolist() == [12, 4]

