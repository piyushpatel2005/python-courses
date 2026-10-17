from solution import *
import matplotlib.pyplot as plt

def test_01_library_panel():
    """Library panel groups branches and starts at zero"""
    for frame, expected in [(pd.DataFrame({'branch':['B','A','B'], 'visits':[3,4,5]}), [4,8]), (pd.DataFrame({'branch':['C','A','C'], 'visits':[5,2,7]}), [2,12])]:
        plt.close('all')
        _, axes = build_dashboard(pd.DataFrame({'day':['01'], 'temp_c':[19]}), frame, pd.DataFrame({'day':['01'], 'rides':[4]}))
        assert [p.get_height() for p in axes[0,1].patches] == expected
        assert axes[0,1].get_ylim()[0] == 0 and axes[0,1].get_ylabel() == 'Visits'

def test_02_transit_panel():
    """Transit panel plots daily sums"""
    for frame, expected in [(pd.DataFrame({'day':['02','01','01'], 'rides':[9,2,3]}), [5,9]), (pd.DataFrame({'day':['B','A','B'], 'rides':[10,1,2]}), [1,12])]:
        plt.close('all')
        figure, axes = build_dashboard(pd.DataFrame({'day':['01'], 'temp_c':[19]}), pd.DataFrame({'branch':['A'], 'visits':[4]}), frame)
        assert len(figure.axes) == 4
        assert list(axes[1,0].lines[0].get_ydata()) == expected
        assert axes[1,0].get_ylabel() == 'Rides' and axes[1,0].get_xlabel() == 'Day'
