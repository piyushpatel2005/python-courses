from solution import *
import pandas as pd

def test_01_one_field():
    """Return the named Series with its values and row labels."""
    table = pd.DataFrame({"x": [4, 7], "y": [8, 9]}, index=["late", "early"])
    for name in table.columns:
        pd.testing.assert_series_equal(one_field(table, name), table[name])

def test_02_report_fields():
    """Keep exactly the requested columns, in the requested order."""
    table = pd.DataFrame({"a": [1, 2], "b": [3, 4], "c": [5, 6]}, index=[20, 10])
    for names in [["c", "a"], ["a"], ["b", "c"], []]:
        pd.testing.assert_frame_equal(report_fields(table, names), table[names])
