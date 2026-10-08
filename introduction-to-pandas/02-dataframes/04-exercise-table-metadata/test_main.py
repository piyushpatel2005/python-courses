from solution import *
import pandas as pd

def test_01_exercise_table_metadata():
    """Make `table_labels(table)` return a pair of lists `(row_labels, column_names)`."""
    assert table_labels(pd.DataFrame({"sold": [5, 7], "open": [True, False]}, index=["a", "b"])) == (["a", "b"], ["sold", "open"]) and table_labels(pd.DataFrame({"day": ["Sat"]})) == ([0], ["day"])

def test_02_exercise_table_metadata():
    """Make `column_dtype(table, column)` return the dtype of the named column."""
    assert pd.api.types.is_bool_dtype(column_dtype(pd.DataFrame({"on": [True], "count": [3]}), "on")) and pd.api.types.is_integer_dtype(column_dtype(pd.DataFrame({"on": [True], "count": [3]}), "count"))

