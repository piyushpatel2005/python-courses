from solution import *
import matplotlib.pyplot as plt

def test_01_matched_not_causal():
    """Only matched days appear, without a causal claim"""
    import numpy as np
    for garden, library, expected in [(pd.DataFrame({'day':['01','02','03'], 'temp_c':[18,20,22]}), pd.DataFrame({'day':['03','01','04'], 'visits':[42,30,99]}), [[18,30],[22,42]]), (pd.DataFrame({'day':['B','A'], 'temp_c':[9,7]}), pd.DataFrame({'day':['A','B'], 'visits':[14,12]}), [[9,12],[7,14]])]:
        plt.close('all')
        _, chart = paired_plot(garden, library)
        assert np.array_equal(chart.collections[0].get_offsets(), expected)
        assert chart.get_title() == 'Matched garden and library days'
