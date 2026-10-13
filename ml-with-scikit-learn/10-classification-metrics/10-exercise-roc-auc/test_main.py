from solution import *

def test_01_behavior():
    """Exercise: measure classification ranking with ROC AUC"""
    for y,s,pos in [([0,1,0,1],[0.1,0.4,0.3,0.8],1), (['yes','no','yes','no'],[0.4,0.4,0.9,0.7],'yes')]:
        got=rank_auc(y,s,pos)
        assert got is not None, 'Use continuous scores.'
        pairs=[float(a>b)+0.5*float(a==b) for a,label in zip(s,y) if label==pos for b,other in zip(s,y) if other!=pos]
        assert np.isclose(got,np.mean(pairs))
        assert np.isclose(rank_auc(y,np.array(s)*3+2,pos),got), 'Rankings survive an increasing transformation.'
