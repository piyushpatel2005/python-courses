from solution import *
import matplotlib.pyplot as plt

def test_01_category_comparison():
    """Bars use all branch rows and begin at zero"""
    for branches, visits in [(['East','West'],[52,84]), (['A','B','C'],[3,8,5])]:
        plt.close('all')
        _, axes = review_charts(branches, visits, [17,20], [30,40])
        assert [bar.get_height() for bar in axes[0].patches] == visits
        assert [t.get_text() for t in axes[0].get_xticklabels()] == branches
        assert axes[0].get_ylim()[0] == 0 and axes[0].get_ylabel() == 'Visits'

def test_02_paired_numeric_view():
    """Scatter keeps numeric pairs with units"""
    import numpy as np
    plt.close('all')
    _, axes = review_charts(['A'], [4], [11,22,30], [5,7,9])
    assert np.array_equal(axes[1].collections[0].get_offsets(), [[11,5],[22,7],[30,9]])
    assert axes[1].get_xlabel() == 'Temperature (°C)' and axes[1].get_ylabel() == 'Visitors'
