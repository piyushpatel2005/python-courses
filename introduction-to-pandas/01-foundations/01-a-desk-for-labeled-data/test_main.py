from solution import *
import pandas as pd

def test_01_a_desk_for_labeled_data():
    """Change the `bread` stall count from 8 to 11."""
    assert isinstance(counts, pd.Series) and counts.to_dict() == {"bread": 11, "flowers": 5}

