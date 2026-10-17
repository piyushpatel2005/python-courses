from solution import *
import matplotlib.pyplot as plt

def test_01_same_readings():
    """Both panels plot all supplied readings"""
    for days, values in [(['Mon', 'Tue', 'Wed'], [19, 20, 21]), (['A', 'B', 'C', 'D'], [18.7, 19.3, 20.1, 21.2])]:
        plt.close('all')
        figure, axes = temperature_context(days, values)
        assert len(figure.axes) == 2
        for chart in axes:
            assert len(chart.lines) == 1
            assert list(chart.lines[0].get_ydata()) == values

def test_02_honest_ranges():
    """Context starts at zero while detail discloses its window"""
    plt.close('all')
    _, axes = temperature_context(['A', 'B'], [12, 14], (10, 16))
    assert axes[0].get_ylim()[0] == 0
    assert axes[1].get_ylim() == (10, 16) and 'Detail' in axes[1].get_title()
