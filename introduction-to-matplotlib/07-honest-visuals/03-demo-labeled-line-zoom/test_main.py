from solution import *
import matplotlib.pyplot as plt

def test_01_disclose_zoom():
    """The zoomed axis and its title agree"""
    for days, values in [(['Mon', 'Tue', 'Wed'], [19.2, 20, 20.4]), (['A', 'B'], [18.5, 21.5])]:
        plt.close('all')
        _, chart = temperature_detail(days, values)
        assert chart.get_ylim() == (18, 22)
        assert 'detail view (18–22 °C)' in chart.get_title()
        assert list(chart.lines[0].get_ydata()) == values
