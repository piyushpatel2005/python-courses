from solution import *
import pandas as pd

def test_stock_cutoff():
    """Keep only stalls with eight or more crates"""
    for frame in [stock, pd.DataFrame({"stall": ["Maple", "Elm", "Pine", "Ash"], "crates": [8, 3, 15, 7]}, index=["m", "e", "p", "a"])]:
        before = frame.copy(deep=True)
        selected_mask, selected_rows = select_stalls(frame)
        pd.testing.assert_series_equal(selected_mask, frame["crates"] >= 8)
        pd.testing.assert_frame_equal(selected_rows, frame.loc[frame["crates"] >= 8])
        pd.testing.assert_frame_equal(frame, before)
    pd.testing.assert_series_equal(mask, stock["crates"] >= 8)
    pd.testing.assert_frame_equal(result, stock.loc[mask])
