from solution import *
import matplotlib.pyplot as plt

def test_01_clean_sums():
    """Daily values are valid ride sums, not row means"""
    for frame, expected in [(pd.DataFrame({'day':['02','01','01','02'], 'route':['A','A','B','B'], 'rides':[64,55,31,None]}), [('01',86),('02',64)]), (pd.DataFrame({'day':['B','A','B','B'], 'route':['X','X','Y',None], 'rides':[4,2,9,100]}), [('A',2),('B',13)])]:
        assert list(daily_transit(frame).itertuples(index=False, name=None)) == expected

def test_02_plot_daily_totals():
    """Line shows grouped rides with markers and units"""
    plt.close('all')
    _, chart = plot_transit(pd.DataFrame({'day':['A','A','B'], 'route':['X','Y','X'], 'rides':[2,5,4]}))
    assert list(chart.lines[0].get_ydata()) == [7,4]
    assert chart.lines[0].get_marker() != 'None' and chart.get_ylabel() == 'Rides'
