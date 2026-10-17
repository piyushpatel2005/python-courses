from solution import *
import matplotlib.pyplot as plt

def test_01_zero_baseline():
    """Bars begin at zero for different counts"""
    for counts in ([5, 8], [12, 17]):
        plt.close('all')
        figure, chart = draw_volunteers(counts)
        assert chart.get_ylim()[0] == 0
        assert [bar.get_height() for bar in chart.patches] == counts
