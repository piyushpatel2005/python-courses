from solution import *
import pandas as pd

def test_01_row_labels():
    """Change unknown to late without changing the table data."""
    pd.testing.assert_frame_equal(table, pd.DataFrame({"stall": ["tea", "honey"], "sold": [5, 8]}, index=["early", "late"]))
