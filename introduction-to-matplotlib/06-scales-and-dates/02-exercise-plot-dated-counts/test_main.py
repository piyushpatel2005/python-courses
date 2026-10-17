from solution import *
import matplotlib.dates as mdates
import numpy as np
import pandas as pd

def test_01_sort_calendar_dates_with_counts():
    data = pd.DataFrame({"day": ["2024-09-12", "2024-09-01", "2024-09-07"], "visits": [60, 20, 45]})
    figure, axis = plot_dated_visits(data)
    assert axis in figure.axes and len(axis.lines) == 1
    assert np.allclose(axis.lines[0].get_xdata(orig=False), mdates.date2num(pd.to_datetime(["2024-09-01", "2024-09-07", "2024-09-12"])))
    assert list(axis.lines[0].get_ydata()) == [20, 45, 60]
    assert data["day"].tolist()[0] == "2024-09-12"

def test_02_date_and_visit_units():
    _, axis = plot_dated_visits(pd.DataFrame({"day": ["2024-01-02"], "visits": [4]}))
    assert axis.get_xlabel() == "Date" and axis.get_ylabel() == "Visits (people)"
