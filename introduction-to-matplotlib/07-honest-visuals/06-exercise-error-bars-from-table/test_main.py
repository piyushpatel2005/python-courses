from solution import *
import matplotlib.pyplot as plt

def test_01_intervals_follow_table():
    """Each supplied margin sets its own interval"""
    import numpy as np
    for frame in [pd.DataFrame({'day':['Mon','Tue'], 'score':[72,75], 'margin':[3,5]}), pd.DataFrame({'day':['A','B','C'], 'score':[35,42,40], 'margin':[1,4,2]})]:
        plt.close('all')
        _, chart = survey_intervals(frame)
        group = chart.containers[0]
        assert list(group.lines[0].get_ydata()) == list(frame['score'])
        assert len(group.lines[1]) == 2
        assert np.allclose([s[1][1]-s[0][1] for s in group.lines[2][0].get_segments()], 2*frame['margin'])

def test_02_units():
    """Labels say what the estimates measure"""
    plt.close('all')
    _, chart = survey_intervals(pd.DataFrame({'day':['Fri'], 'score':[50], 'margin':[2]}))
    assert chart.get_xlabel() == 'Day' and chart.get_ylabel() == 'Survey score (points)'
