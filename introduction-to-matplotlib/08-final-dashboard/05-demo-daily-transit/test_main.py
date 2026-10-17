from solution import *
import matplotlib.pyplot as plt

def test_01_marked_daily_sums():
    """Daily sums and markers adapt to new route rows"""
    for frame, totals in [(pd.DataFrame({'day':['01','01','02'], 'rides':[55,31,64]}), [86,64]), (pd.DataFrame({'day':['B','A','B'], 'rides':[4,2,9]}), [2,13])]:
        plt.close('all')
        _, chart = transit_line(frame)
        assert list(chart.lines[0].get_ydata()) == totals
        assert chart.lines[0].get_marker() == 'o'
