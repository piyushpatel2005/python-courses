from solution import *
import pandas as pd

def test_01_exercise_import_pandas():
    """Make `count_card(values)` return a pandas Series containing the supplied values in order."""
    assert isinstance(count_card([3, 8]), pd.Series) and count_card([3, 8]).tolist() == [3, 8] and count_card([]).empty

