from solution import *
import matplotlib.pyplot as plt

def test_01_clean_and_match():
    """Inputs are cleaned and grouped without fixed totals"""
    for garden, library, transit, expected in [
        (pd.DataFrame({'day':['01','01','02'], 'temp_c':[18,20,None]}), pd.DataFrame({'day':['01','01','02'], 'branch':['A','B','A'], 'visits':[10,7,None]}), pd.DataFrame({'day':['01','01','02'], 'route':['X','Y','X'], 'rides':[5,3,None]}), (['01'], [19], [10,7], [8], [17])),
        (pd.DataFrame({'day':['B','A','B'], 'temp_c':[20,10,24]}), pd.DataFrame({'day':['A','B','B'], 'branch':['X','X','Y'], 'visits':[4,5,6]}), pd.DataFrame({'day':['A','B','B'], 'route':['R','R','S'], 'rides':[1,9,2]}), (['A','B'], [10,22], [9,6], [1,11], [4,11]))
    ]:
        gd, branches, rides, matched = prepare_signals(garden, library, transit)
        days, temps, branch_values, ride_values, pair_visits = expected
        assert list(gd['day']) == days and list(gd['temp_c']) == temps
        assert list(branches.values) == branch_values and list(rides.values) == ride_values
        assert list(matched['visits']) == pair_visits

def test_02_four_labeled_panels():
    """All panels show prepared signals with legible units and a zero bar"""
    import numpy as np
    plt.close('all')
    garden = pd.DataFrame({'day':['01','01','02'], 'temp_c':[18,20,22]})
    library = pd.DataFrame({'day':['01','02','02'], 'branch':['A','A','B'], 'visits':[5,8,4]})
    transit = pd.DataFrame({'day':['01','01','02'], 'route':['R','S','R'], 'rides':[6,2,7]})
    figure, axes = build_dashboard(garden, library, transit)
    assert axes.shape == (2,2) and len(figure.axes) == 4
    assert list(axes[0,0].lines[0].get_ydata()) == [19,22]
    assert [p.get_height() for p in axes[0,1].patches] == [13,4]
    assert axes[0,1].get_ylim()[0] == 0
    assert list(axes[1,0].lines[0].get_ydata()) == [8,7]
    assert np.array_equal(axes[1,1].collections[0].get_offsets(), [[19,5],[22,12]])
    assert [a.get_ylabel() for a in axes.flat] == ['Temperature (°C)','Visits','Rides','Visits']
    assert all(a.get_legend() for a in (axes[0,0], axes[1,0], axes[1,1]))
