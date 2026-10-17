from solution import *
import matplotlib.pyplot as plt

def test_01_join_summed_days():
    """Visit totals and garden dates form real shared-day pairs"""
    for garden, library, expected in [(pd.DataFrame({'day':['01','02','03'], 'temp_c':[18,20,22]}), pd.DataFrame({'day':['02','01','02'], 'visits':[31,24,12]}), [('01',18,24),('02',20,43)]), (pd.DataFrame({'day':['B','A'], 'temp_c':[15,12]}), pd.DataFrame({'day':['A','A','B','X'], 'visits':[3,4,5,99]}), [('B',15,5),('A',12,7)])]:
        assert list(match_signals(garden, library).itertuples(index=False, name=None)) == expected

def test_02_scatter_pairs_and_units():
    """Points match shared days without implying causation"""
    import numpy as np
    plt.close('all')
    garden = pd.DataFrame({'day':['B','A'], 'temp_c':[15,12]})
    library = pd.DataFrame({'day':['A','A','B'], 'visits':[3,4,5]})
    _, chart = signal_scatter(garden, library)
    assert np.array_equal(chart.collections[0].get_offsets(), [[15,5],[12,7]])
    assert chart.get_xlabel() == 'Temperature (°C)' and chart.get_ylabel() == 'Visits'
    assert 'drives' not in chart.get_title().lower()
