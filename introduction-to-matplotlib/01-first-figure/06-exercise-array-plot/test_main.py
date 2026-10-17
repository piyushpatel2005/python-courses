from solution import *
import matplotlib.pyplot as plt
import numpy as np

def test_01_exercise_array_plot():
    """Complete `temperature_figure(hours, temperatures)` to plot the two arrays and return the figure."""
    try:
        for hours, temperatures in [(np.array([8, 10, 12]), np.array([15, 18, 22])), (np.array([6, 13]), np.array([11, 24]))]:
            chart = temperature_figure(hours, temperatures)
            assert isinstance(chart, plt.Figure) and len(chart.axes) == 1
            assert len(chart.axes[0].lines) == 1
            assert list(chart.axes[0].lines[0].get_xdata()) == list(hours)
            assert list(chart.axes[0].lines[0].get_ydata()) == list(temperatures)
    finally:
        plt.close('all')
