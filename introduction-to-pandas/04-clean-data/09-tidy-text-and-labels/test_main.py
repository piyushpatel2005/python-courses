from solution import *
import pandas as pd

def test_normalized_vendors():
    """Keep clean, lowercase names with the new header and category"""
    expected = pd.DataFrame({"vendor": ["mina", "sol"], "category": ["produce", "bread"]})
    pd.testing.assert_frame_equal(result, expected)
