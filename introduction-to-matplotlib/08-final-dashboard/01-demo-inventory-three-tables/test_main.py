from solution import *
import matplotlib.pyplot as plt

def test_01_title_and_readings():
    """Garden preview names units and follows supplied readings"""
    for values in ([18,20,19], [12,14,13]):
        plt.close('all')
        garden = pd.DataFrame({'day':['Mon','Tue','Wed'], 'temp_c':values})
        _, chart = garden_preview(garden, pd.DataFrame(), pd.DataFrame())
        assert chart.get_title() == 'Garden temperature (°C)'
        assert list(chart.lines[0].get_ydata()) == values
