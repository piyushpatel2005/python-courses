from solution import *

def test_01_behavior():
    """Keep entities out of both sides"""
    for counts in [[2,3,4,5,6,7],[5,5,5,5,5,5]]:
        groups=np.concatenate([np.repeat(i,n) for i,n in enumerate(counts)])
        X=np.arange(len(groups)).reshape(-1,1)
        folds=entity_folds(X,groups)
        assert folds is not None, 'Return the fold index pairs.'
        assert len(folds)==3
        assert sorted(np.concatenate([va for tr,va in folds]))==list(range(len(groups)))
        for tr,va in folds:
            assert not set(groups[tr])&set(groups[va]), 'An entity must not cross a fold boundary.'
            assert set(tr)|set(va)==set(range(len(groups)))
