from solution import *

def test_01_behavior():
    """Exercise: evaluate whole pipelines in folds"""
    for n in [30,42]:
        X=np.arange(n*2,dtype=float).reshape(n,2); y=np.sin(X[:,0])+X[:,0]
        result=evaluate_folds(X,y)
        assert result is not None, 'Return folds, positive errors, and fitted estimators.'
        folds, errors, models=result
        assert len(folds)==len(errors)==len(models)==3
        assert sorted(np.concatenate([va for tr,va in folds]))==list(range(n))
        for (tr,va),error,model in zip(folds,errors,models):
            assert not set(tr)&set(va)
            assert np.isclose(error,np.mean(np.abs(y[va]-model.predict(X[va]))))
            assert np.allclose(model.named_steps['scale'].mean_,X[tr].mean(axis=0))
