from solution import *
import pandas as pd

def test_required_email():
    """Remove only rows missing an email"""
    pd.testing.assert_frame_equal(result, signups.dropna(subset=["email"]))
