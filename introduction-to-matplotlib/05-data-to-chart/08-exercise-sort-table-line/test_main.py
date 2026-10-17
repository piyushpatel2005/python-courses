from solution import *
import pandas as pd

def test_01_sort_whole_rows_on_new_frame():
    data = pd.DataFrame({"day": [9, 2, 5, 1], "parcels": [40, 30, 10, 20]})
    _, axis = plot_parcels(data)
    assert len(axis.lines) == 1
    assert list(axis.lines[0].get_xdata()) == [1, 2, 5, 9]
    assert list(axis.lines[0].get_ydata()) == [20, 30, 10, 40]
    assert data["day"].tolist() == [9, 2, 5, 1]

def test_02_named_units():
    _, axis = plot_parcels(pd.DataFrame({"day": [1], "parcels": [2]}))
    assert axis.get_xlabel() == "Day" and axis.get_ylabel() == "Parcels (boxes)"
