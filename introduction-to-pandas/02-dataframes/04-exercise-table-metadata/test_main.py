from solution import *
import pandas as pd

def test_01_table_labels():
    """Return row labels and column names as a pair of lists."""
    for table in [pd.DataFrame({"sold": [5, 7], "open": [True, False]}, index=["a", "b"]), pd.DataFrame({"day": ["Sat"]}), pd.DataFrame({"empty": []})]:
        assert table_labels(table) == (table.index.tolist(), table.columns.tolist())

def test_02_column_dtype():
    """Return the selected dtype object, not its printed name."""
    table = pd.DataFrame({"on": [True], "count": [3], "price": [2.5], "stall": ["tea"]})
    for column in table.columns:
        actual = column_dtype(table, column)
        assert not isinstance(actual, str), "Return the dtype object, not a string."
        assert actual == table.dtypes.loc[column]
