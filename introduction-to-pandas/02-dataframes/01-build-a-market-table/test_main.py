from solution import *
import pandas as pd

def test_01_column_table():
    """Change bread to 9 in the column-based table."""
    pd.testing.assert_frame_equal(stalls, pd.DataFrame({"stall": ["tea", "bread"], "visitors": [4, 9]}))

def test_02_record_table():
    """Change bread to 9 in the row-based table."""
    pd.testing.assert_frame_equal(records, pd.DataFrame({"stall": ["tea", "bread"], "visitors": [4, 9]}))
