from solution import *
import pandas as pd

def test_01_select_a_column():
    """Set `chosen` to the `sold` column as a Series."""
    assert isinstance(chosen, pd.Series) and chosen.name == "sold" and chosen.tolist() == [3, 9]

