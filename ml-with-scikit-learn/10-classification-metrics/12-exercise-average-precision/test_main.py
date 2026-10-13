from solution import *

def test_01_behavior():
    """Exercise: summarize precision-recall rankings"""
    for y,s,expected in [([1,0,1,0],[0.9,0.8,0.7,0.1],(1+2/3)/2),([0,1,0,1],[0.9,0.8,0.7,0.6],0.5),([1,0,1,0],[0.5]*4,0.5)]:
        got=ranking_ap(y,s,1)
        assert got is not None, 'Return average precision.'
        assert np.isclose(got,expected), 'Weight precision by recall increments, including tied scores.'
    assert np.isclose(ranking_ap(['return','keep','return','keep'],[9,8,7,1],'return'),5/6)
