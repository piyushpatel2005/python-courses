from solution import *
import pandas as pd

def test_01_complete_rows_from_changed_data():
    data = pd.DataFrame({"rain_mm": [0, 4, None, 8, 10], "visitors": [72, None, 44, 30, 18]})
    figure, axis = plot_rain_visitors(data)
    assert axis in figure.axes and len(axis.collections) == 1
    assert axis.collections[0].get_offsets().tolist() == [[0, 72], [8, 30], [10, 18]]
    assert len(data) == 5

def test_02_units():
    _, axis = plot_rain_visitors(pd.DataFrame({"rain_mm": [2], "visitors": [9]}))
    assert axis.get_xlabel() == "Rainfall (mm)" and axis.get_ylabel() == "Visitors (people)"
