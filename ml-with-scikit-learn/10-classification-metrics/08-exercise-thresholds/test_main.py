from solution import *

def test_01_behavior():
    """Exercise: choose a decision threshold"""
    for y,scores,minimum in [([1,0],[0.3,0.1],0.75),([1,1,0],[0.5,0.7,0.2],0.75),([1,1,0],[0.1,0.2,0.9],0.75),([1,0],[0.9,0.8],0.75)]:
        got=choose_threshold(y,scores,minimum)
        assert got is not None, 'Return one candidate threshold.'
        rows=[]
        for t in [0.3,0.5,0.7]:
            pred=np.array(scores)>=t
            tp=np.sum(pred & (np.array(y)==1))
            rows.append((t,tp/max(np.sum(pred),1),tp/max(sum(y),1)))
        good=[r for r in rows if r[2]>=minimum]
        expected=sorted(good,key=lambda r:(-r[1],-r[0]))[0][0] if good else sorted(rows,key=lambda r:(-r[2],-r[1],r[0]))[0][0]
        assert got==expected, 'Check the >= boundary, recall constraint, and tie rules.'
