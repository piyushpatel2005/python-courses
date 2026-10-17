from solution import *
import matplotlib.pyplot as plt

def test_01_descriptive_legend():
    """Both routes appear in a legend and have different styles"""
    for east, west in [([12,16,14],[8,11,13]), ([1,3,2],[3,2,1])]:
        plt.close('all')
        _, chart = route_compare(['Mon','Tue','Wed'], east, west)
        assert [t.get_text() for t in chart.get_legend().get_texts()] == ['East route', 'West route']
        assert chart.lines[0].get_linestyle() != chart.lines[1].get_linestyle()
        assert list(chart.lines[1].get_ydata()) == west
