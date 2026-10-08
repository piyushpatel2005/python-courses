from solution import *
import pandas as pd

def test_safe_review_assignment():
    """Update only low-stock rows while leaving source alone"""
    expected = stock.copy()
    expected.loc[expected["units"] < 3, "status"] = "review"
    pd.testing.assert_frame_equal(cleaned, expected)
    assert stock["status"].tolist() == ["ok", "ok", "ok"]
