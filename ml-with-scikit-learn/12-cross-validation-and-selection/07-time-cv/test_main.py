from solution import *

def test_01_behavior():
    """Validate on later observations"""
    for n in [24,36,60]:
        X=np.arange(n).reshape(-1,1)
        folds=future_folds(X)
        assert folds is not None, 'Return chronological folds.'
        assert len(folds)==3
        for tr,va in folds:
            assert len(va)==4 and max(tr)+2==min(va), 'Leave exactly one excluded row.'
            assert np.array_equal(tr,np.arange(len(tr)))
            assert max(tr)<min(va)
        assert folds[-1][1][-1]==n-1
