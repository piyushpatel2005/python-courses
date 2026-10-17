from solution import *
import numpy as np
import matplotlib.dates as mdates

def test_01_calendar_coordinates_and_marker():
    assert ax is fig.axes[0] and len(ax.lines) == 1
    line = ax.lines[0]
    assert np.allclose(line.get_xdata(orig=False), mdates.date2num(dates))
    assert list(line.get_ydata()) == [12, 14, 17] and line.get_marker() == "s"
