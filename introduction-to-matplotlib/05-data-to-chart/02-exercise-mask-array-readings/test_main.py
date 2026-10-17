from solution import *
import numpy as np

def test_01_mask_both_arrays_on_changed_data():
    figure, axes = plot_loud_days(np.array([11, 12, 13, 14]), np.array([61, 40, 75, 61]), 61)
    assert axes in figure.axes and len(axes.lines) == 1
    assert list(axes.lines[0].get_xdata()) == [13]
    assert list(axes.lines[0].get_ydata()) == [75]
    other, axis = plot_loud_days(np.array([4, 8, 12]), np.array([90, 70, 80]), 75)
    assert list(axis.lines[0].get_xdata()) == [4, 12]
    assert list(axis.lines[0].get_ydata()) == [90, 80]

def test_02_label_units():
    _, axis = plot_loud_days([1, 2], [55, 61], 50)
    assert axis.get_xlabel() == "Day" and axis.get_ylabel() == "Noise (dB)"
