from solution import *
import pandas as pd

def test_both_rules():
    """Keep only the stall satisfying both rules"""
    pd.testing.assert_frame_equal(result, table.loc[(table["baskets"] >= 4) & (table["aisle"] == "east")])
