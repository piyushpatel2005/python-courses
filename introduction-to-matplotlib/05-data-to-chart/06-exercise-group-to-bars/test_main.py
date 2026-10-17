from solution import *
import pandas as pd

def test_01_dynamic_grouped_bars():
    frame = pd.DataFrame({"route": ["Z", "A", "Z", "B", "A"], "minutes": [9, 6, 21, 12, 18]})
    figure, axis = plot_route_means(frame)
    assert axis in figure.axes and len(axis.patches) == 3
    assert [tick.get_text() for tick in axis.get_xticklabels()] == ["A", "B", "Z"]
    assert [bar.get_height() for bar in axis.patches] == [12, 12, 15]
    frame.loc[0, "minutes"] = 39
    _, changed = plot_route_means(frame)
    assert [bar.get_height() for bar in changed.patches] == [12, 12, 30]

def test_02_labels():
    _, axis = plot_route_means(pd.DataFrame({"route": ["N"], "minutes": [7]}))
    assert axis.get_xlabel() == "Route" and axis.get_ylabel() == "Mean trip (minutes)"
