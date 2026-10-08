from solution import *
import pandas as pd

def test_integer_tickets():
    """Invalid numeric text becomes zero in an integer Series"""
    pd.testing.assert_series_equal(result, pd.Series([12, 0, 9], name="tickets", dtype="int64"))
