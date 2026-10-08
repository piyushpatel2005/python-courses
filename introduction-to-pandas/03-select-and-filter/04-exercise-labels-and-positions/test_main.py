from solution import *
import pandas as pd

def test_label_window():
    """Labels include stop and retain named columns"""
    for names, start, stop in [(["dawn", "noon", "night"], "dawn", "noon"), (["a", "b", "c", "d"], "b", "d")]:
        frame = pd.DataFrame({"item": list(names), "count": range(len(names)), "dock": ["X"] * len(names)}, index=names)
        pd.testing.assert_frame_equal(label_window(frame, start, stop), frame.loc[start:stop, ["item", "count"]])

def test_position_window():
    """Positions exclude stop even with nonnumeric labels"""
    for start, stop in [(1, 3), (0, 2)]:
        frame = pd.DataFrame({"item": ["A", "B", "C", "D"], "count": [1, 2, 3, 4], "dock": ["W"] * 4}, index=["z", "a", "r", "p"])
        pd.testing.assert_frame_equal(position_window(frame, start, stop), frame.iloc[start:stop, :2])
