from solution import *
import pandas as pd

def test_01_index_and_values_on_changed_series():
    _, axis = plot_visits(pd.Series([7, 19, 4], index=["West", "East", "Central"]))
    assert len(axis.lines) == 1
    line = axis.lines[0]
    assert list(line.get_xdata()) == ["West", "East", "Central"]
    assert list(line.get_ydata()) == [7, 19, 4] and line.get_marker() == "o"

def test_02_named_axes():
    _, axis = plot_visits(pd.Series([1], index=["West"]))
    assert axis.get_xlabel() == "Neighborhood" and axis.get_ylabel() == "Visits (people)"
