from solution import *
import matplotlib.pyplot as plt

def test_01_totals_and_zero():
    """Grouped bars retain proportional lengths from zero"""
    for frame, expected in [(pd.DataFrame({'branch':['East','West','East'], 'visits':[32,45,39]}), [71,45]), (pd.DataFrame({'branch':['A','B','A'], 'visits':[2,8,5]}), [7,8])]:
        plt.close('all')
        _, chart = branch_totals(frame)
        assert chart.get_ylim()[0] == 0
        assert [p.get_height() for p in chart.patches] == expected
