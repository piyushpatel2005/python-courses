from solution import *
import matplotlib.pyplot as plt

def test_01_daily_average():
    """Missing values are omitted and repeated days averaged"""
    for frame, expected in [(pd.DataFrame({'day':['02','01','01','03'], 'temp_c':[21,18,20,None]}), [('01',19),('02',21)]), (pd.DataFrame({'day':['B','A','B','A','C'], 'temp_c':[10,4,14,None,20]}), [('A',4),('B',12),('C',20)])]:
        assert list(daily_garden(frame).itertuples(index=False, name=None)) == expected

def test_02_daily_line():
    """Line uses grouped temperatures and clear units"""
    plt.close('all')
    frame = pd.DataFrame({'day':['B','A','A'], 'temp_c':[17,19,21]})
    _, chart = garden_line(frame)
    assert list(chart.lines[0].get_ydata()) == [20,17]
    assert chart.get_ylabel() == 'Temperature (°C)'
