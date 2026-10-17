from solution import *
import matplotlib.pyplot as plt

def test_01_clean_grouped_totals():
    """Groups all valid rows and excludes missing branch or count"""
    for frame, expected in [(pd.DataFrame({'branch':['East','West','East',None], 'visits':[30,42,14,8]}), [('East',44),('West',42)]), (pd.DataFrame({'branch':['B','A','B','A'], 'visits':[2,3,None,4]}), [('A',7),('B',2)])]:
        assert list(library_totals(frame).items()) == expected

def test_02_bars_show_totals():
    """Bar heights and units reflect the aggregation"""
    plt.close('all')
    _, chart = library_bars(pd.DataFrame({'branch':['A','B','A'], 'visits':[5,8,4]}))
    assert [p.get_height() for p in chart.patches] == [9,8]
    assert chart.get_ylim()[0] == 0 and chart.get_ylabel() == 'Visits'
