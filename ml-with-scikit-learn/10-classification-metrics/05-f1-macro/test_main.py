from solution import *

def test_01_behavior():
    """Summarize multiclass errors"""
    for y,pred in [([0,0,0,0,1],[0,0,0,1,0]), ([0,1,2,2,2],[0,2,2,1,2])]:
        labels=np.unique(y)
        result=class_report(y,pred,labels)
        assert result is not None, 'Return class values, macro mean, and supports.'
        values, macro, support=result
        expected=[]
        for label in labels:
            tp=sum(a==label and b==label for a,b in zip(y,pred))
            den=sum(a==label for a in y)+sum(b==label for b in pred)
            expected.append(2*tp/den if den else 0)
        assert np.shape(values)==(len(labels),)
        assert np.allclose(values,expected) and np.isclose(macro,np.mean(expected))
        assert np.array_equal(support,[list(y).count(x) for x in labels])
