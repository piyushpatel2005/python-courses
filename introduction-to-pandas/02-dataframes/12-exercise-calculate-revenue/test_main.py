from solution import *
import pandas as pd

def test_01_revenue():
    """Add revenue without losing existing data or row labels."""
    for table in [pd.DataFrame({"sold": [2, 5], "price": [3, 4]}, index=["tea", "jam"]), pd.DataFrame({"sold": [7, 0], "price": [2.5, 9.0], "stall": ["soap", "rice"]}, index=[20, 10]), pd.DataFrame({"sold": [], "price": []})]:
        expected = table.copy()
        expected["revenue"] = expected["sold"] * expected["price"]
        pd.testing.assert_frame_equal(with_revenue(table), expected)
