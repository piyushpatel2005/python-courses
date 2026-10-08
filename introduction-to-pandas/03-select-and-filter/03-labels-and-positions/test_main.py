from solution import *
import pandas as pd

def test_inclusive_label_end():
    """Label window includes the ending label"""
    pd.testing.assert_frame_equal(result, ledger.loc["early":"mid", ["stall", "sales"]])
