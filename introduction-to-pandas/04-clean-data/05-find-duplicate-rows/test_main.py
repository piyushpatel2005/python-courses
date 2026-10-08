from solution import *
import pandas as pd

def test_visit_key():
    """Retain the Saturday visit while removing Friday's repeat"""
    pd.testing.assert_frame_equal(result, visits.drop_duplicates(subset=["stall", "day"]))
