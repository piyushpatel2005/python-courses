from solution import *
import pandas as pd

def test_01_exercise_calculate_revenue():
    """Make `with_revenue(table)` return a table with a `revenue` column equal to `sold * price` for each row."""
    assert isinstance(with_revenue(pd.DataFrame({"sold": [2, 5], "price": [3, 4]}, index=["tea", "jam"])), pd.DataFrame) and with_revenue(pd.DataFrame({"sold": [2, 5], "price": [3, 4]}, index=["tea", "jam"]))["revenue"].tolist() == [6, 20] and with_revenue(pd.DataFrame({"sold": [7, 1], "price": [2, 9]}, index=["a", "b"]))["revenue"].tolist() == [14, 9] and with_revenue(pd.DataFrame({"sold": [2], "price": [8], "stall": ["tea"]}, index=["x"])).index.tolist() == ["x"] and "stall" in with_revenue(pd.DataFrame({"sold": [2], "price": [8], "stall": ["tea"]}, index=["x"])).columns

