from solution import *
import pandas as pd

def test_01_read_a_default_index():
    """Change the last receipt total from 7 to 10 without supplying an index."""
    assert isinstance(receipts, pd.Series) and receipts.index.tolist() == [0, 1, 2] and receipts.tolist() == [5, 8, 10]

