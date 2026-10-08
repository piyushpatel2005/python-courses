from solution import *
import pandas as pd

def test_card_columns():
    """Card keeps stall and zone in the requested order"""
    pd.testing.assert_frame_equal(result, roster[["stall", "zone"]])
