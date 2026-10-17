from solution import *
import matplotlib.pyplot as plt

def test_01_series_from_columns():
    """Both lines use the supplied frame rather than fixed readings"""
    for frame in [pd.DataFrame({'day':['Mon','Tue','Wed'], 'east':[12,16,14], 'west':[8,11,13]}), pd.DataFrame({'day':['Fri','Sat'], 'east':[3,9], 'west':[10,6]})]:
        plt.close('all')
        _, chart = accessible_routes(frame)
        assert len(chart.lines) == 2
        assert list(chart.lines[0].get_ydata()) == list(frame['east'])
        assert list(chart.lines[1].get_ydata()) == list(frame['west'])
        assert [line.get_label() for line in chart.lines] == ['East route', 'West route']

def test_02_noncolor_cues():
    """Legend, markers, and line styles distinguish routes"""
    plt.close('all')
    _, chart = accessible_routes(pd.DataFrame({'day':['A','B'], 'east':[1,2], 'west':[2,1]}))
    assert chart.get_legend() is not None
    assert chart.lines[0].get_marker() != chart.lines[1].get_marker()
    assert chart.lines[0].get_linestyle() != chart.lines[1].get_linestyle()
