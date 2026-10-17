from solution import *
import matplotlib.pyplot as plt

def test_01_bins_preserve_counts():
    """Five bins retain observations inside the stated range"""
    for waits in ([2, 3, 5, 8, 12, 17], [1, 1, 2, 6, 10, 11, 16, 19]):
        plt.close('all')
        _, chart = wait_histogram(waits)
        assert len(chart.patches) == 5
        assert sum(p.get_height() for p in chart.patches) == len(waits)
        assert chart.get_xlabel() == 'Minutes'
