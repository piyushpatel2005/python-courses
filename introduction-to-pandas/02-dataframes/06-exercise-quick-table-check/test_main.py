from solution import *
import pandas as pd

def test_01_exercise_quick_table_check():
    """Make `ends(table, amount)` return `(table.head(amount), table.tail(amount))`."""
    assert all(isinstance(part, pd.DataFrame) for part in ends(pd.DataFrame({"x": [4, 8, 12]}, index=["a", "b", "c"]), 2)) and ends(pd.DataFrame({"x": [4, 8, 12]}, index=["a", "b", "c"]), 2)[0].index.tolist() == ["a", "b"] and ends(pd.DataFrame({"x": [4, 8, 12]}, index=["a", "b", "c"]), 2)[1].index.tolist() == ["b", "c"] and ends(pd.DataFrame({"x": [4, 8, 12]}, index=["a", "b", "c"]), 1)[1]["x"].tolist() == [12]

def test_02_exercise_quick_table_check():
    """Make `numeric_summary(table)` return the DataFrame produced by `table.describe()` for its numeric columns."""
    tables = [
        pd.DataFrame({"kind": ["a", "b", "c"], "count": [3, 9, 6]}, index=list("abc")),
        pd.DataFrame({"count": [10, 20], "price": [1.5, 4.5]}, index=list("xy")),
        pd.DataFrame({"price": [2.0, 7.0, 11.0, 5.0], "stock": [0, 1, 1, 9]}),
    ]
    for table in tables:
        before = table.copy(deep=True)
        pd.testing.assert_frame_equal(numeric_summary(table), table.describe())
        pd.testing.assert_frame_equal(table, before)

