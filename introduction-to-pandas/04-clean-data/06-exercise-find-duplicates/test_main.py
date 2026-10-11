from solution import *
import pandas as pd

def test_older_revisions():
    """Mark earlier occurrences of each two-column key"""
    for keys in [[("A", "Fri"), ("A", "Sat"), ("A", "Fri")], [("B", "Sun"), ("B", "Sun"), ("C", "Sun"), ("B", "Sun")]]:
        frame = pd.DataFrame({"order": [x for x, y in keys], "date": [y for x, y in keys], "bags": range(len(keys))}, index=[f"k{i}" for i in range(len(keys))])
        pd.testing.assert_series_equal(older_revisions(frame), frame.duplicated(subset=["order", "date"], keep="last"))

def test_latest_revisions():
    """Keep the final row for each order and date"""
    for keys in [[("A", "Fri"), ("A", "Sat"), ("A", "Fri")], [("B", "Sun"), ("B", "Sun"), ("C", "Sun"), ("B", "Sun")]]:
        frame = pd.DataFrame({"order": [x for x, y in keys], "date": [y for x, y in keys], "bags": range(len(keys))}, index=[f"k{i}" for i in range(len(keys))])
        pd.testing.assert_frame_equal(latest_revisions(frame), frame.drop_duplicates(subset=["order", "date"], keep="last"))
