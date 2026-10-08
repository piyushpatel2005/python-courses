from solution import *
import pandas as pd

def test_descending_order():
    """Show the highest sales first"""
    pd.testing.assert_frame_equal(result, sales.sort_values("sales", ascending=False))
