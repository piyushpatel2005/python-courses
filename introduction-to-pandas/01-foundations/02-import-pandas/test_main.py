from solution import *
import pandas as pd

def test_01_import_pandas():
    """Change the last count in `counts` from 3 to 7."""
    assert isinstance(counts, pd.Series) and counts.tolist() == [4, 6, 7]

