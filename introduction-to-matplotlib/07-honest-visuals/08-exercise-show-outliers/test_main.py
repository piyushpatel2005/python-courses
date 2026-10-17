from solution import *
import matplotlib.pyplot as plt

def test_01_complete_histogram():
    """Full panel keeps every wait, including outliers"""
    for waits, cutoff in [([2,3,6,7,12,39], 20), ([1,4,25,48,60], 30)]:
        plt.close('all')
        _, axes = wait_views(waits, cutoff)
        assert len(axes[0].patches) == 5
        assert sum(p.get_height() for p in axes[0].patches) == len(waits)
        assert abs(max(p.get_x()+p.get_width() for p in axes[0].patches) - max(waits)) < 1e-8

def test_02_detail_disclosure():
    """Detail panel counts only included waits and discloses omissions"""
    for waits, cutoff in [([2,3,6,7,12,39],20), ([1,4,25,48,60],30)]:
        plt.close('all')
        _, axes = wait_views(waits, cutoff)
        kept = sum(w <= cutoff for w in waits)
        assert sum(p.get_height() for p in axes[1].patches) == kept
        assert f'{len(waits)-kept} excluded' in axes[1].get_title()
        assert str(cutoff) in axes[1].get_title()
