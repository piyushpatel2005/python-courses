from solution import *
import pandas as pd

def test_01_from_columns():
    """Build a table from all supplied column lists."""
    for columns in [{"fruit": ["fig", "pear"], "boxes": [2, 7]}, {"price": [5]}, {"item": [], "count": []}]:
        pd.testing.assert_frame_equal(from_columns(columns), pd.DataFrame(columns))

def test_02_from_records():
    """Build a table from all supplied row records."""
    for records in [[{"name": "tea", "sold": 4}, {"name": "jam", "sold": 8}], [{"day": "Fri"}], []]:
        pd.testing.assert_frame_equal(from_records(records), pd.DataFrame(records))
