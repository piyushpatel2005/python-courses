from solution import *
import pandas as pd
import numpy as np
import matplotlib.dates as mdates

def test_01_real_dates_and_rotated_labels():
    frame = pd.DataFrame({"day": ["2024-07-01", "2024-07-11", "2024-07-30"], "bags": [18, 5, 23]})
    _, axis = plot_collection_dates(frame)
    assert len(axis.lines) == 1
    assert np.allclose(axis.lines[0].get_xdata(orig=False), mdates.date2num(pd.to_datetime(frame["day"])))
    assert list(axis.lines[0].get_ydata()) == [18, 5, 23]
    assert axis.get_xticklabels() and all(round(t.get_rotation()) == 40 for t in axis.get_xticklabels())

def test_02_clear_units():
    _, axis = plot_collection_dates(pd.DataFrame({"day": ["2024-01-01"], "bags": [3]}))
    assert axis.get_xlabel() == "Date" and axis.get_ylabel() == "Collected bags (count)"
