from solution import *
import pandas as pd

def test_01_add_aligned_counts():
    """Change the `north` entry of `afternoon` from 2 to 5 so the combined `north` total is 9."""
    assert isinstance(total, pd.Series) and total.to_dict() == {"north": 9, "south": 10}

