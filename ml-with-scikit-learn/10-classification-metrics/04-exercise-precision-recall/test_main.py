from solution import *

def test_01_behavior():
    """Exercise: separate precision and recall"""
    for y, pred, pos in [([0,1,1,0],[1,1,0,0],1), ([0,1,1,0],[1,1,1,1],1), ([0,0],[0,0],1), (['hit','miss','hit'],['miss','miss','hit'],'hit')]:
        result = measure(y,pred,pos)
        assert result is not None, 'Return both rates.'
        tp=sum(a==pos and b==pos for a,b in zip(y,pred))
        pp=sum(b==pos for b in pred); ap=sum(a==pos for a in y)
        expected=(tp/pp if pp else 0, tp/ap if ap else 0)
        assert np.allclose(result, expected), 'Use the selected positive class and zero-denominator policy.'
