from solution import *
import pandas as pd

def test_01_changed_scatter_pairs():
    data = pd.DataFrame({"canopy_pct": [55, 12, 88], "temp_c": [21, 32, 18]})
    _, axis = plot_canopy_temperature(data)
    assert len(axis.collections) == 1
    assert axis.collections[0].get_offsets().tolist() == [[55, 21], [12, 32], [88, 18]]

def test_02_labeled_units():
    _, axis = plot_canopy_temperature(pd.DataFrame({"canopy_pct": [2], "temp_c": [4]}))
    assert axis.get_xlabel() == "Canopy (%)" and axis.get_ylabel() == "Temperature (°C)"
