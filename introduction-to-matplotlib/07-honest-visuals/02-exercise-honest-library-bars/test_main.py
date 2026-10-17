from solution import *
import matplotlib.pyplot as plt

def test_01_bars_follow_rows():
    """Bar heights follow changed branch data"""
    for names, values in [(['East', 'West'], [42, 67]), (['Annex', 'Central', 'North'], [9, 24, 15])]:
        plt.close('all')
        figure, chart = branch_bars(pd.DataFrame({'branch': names, 'visits': values}))
        assert [p.get_height() for p in chart.patches] == values
        figure.canvas.draw()
        assert [t.get_text() for t in chart.get_xticklabels()] == names

def test_02_units_and_baseline():
    """A magnitude axis names visits and begins at zero"""
    plt.close('all')
    _, chart = branch_bars(pd.DataFrame({'branch': ['A'], 'visits': [91]}))
    assert chart.get_ylabel() == 'Visits' and chart.get_ylim()[0] == 0
