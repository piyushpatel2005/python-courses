from solution import *
import pandas as pd

def test_01_build_a_market_table():
    """Change bread visitors in both representations of the same table."""
    expected = pd.DataFrame({"stall": ["tea", "bread"], "visitors": [4, 9]})
    pd.testing.assert_frame_equal(stalls, expected)
    pd.testing.assert_frame_equal(records, expected)

