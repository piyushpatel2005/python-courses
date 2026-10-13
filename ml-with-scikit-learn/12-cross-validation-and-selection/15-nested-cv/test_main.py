from solution import *

def test_01_behavior():
    """Evaluate the model-selection procedure"""
    for n in [32,48]:
        X=np.arange(n*2,dtype=float).reshape(n,2); y=np.sin(X[:,0])+X[:,0]
        result=nested_scores(X,y)
        assert result is not None, 'Return outer folds, errors, and searches.'
        folds,errors,searches=result
        assert len(folds)==len(errors)==len(searches)==2
        for (tr,va),error,search in zip(folds,errors,searches):
            assert not set(tr)&set(va) and search.n_splits_==2
            assert search.param_grid=={'ridge__alpha':[0.1,10.0]} and search.n_jobs==1
            assert np.isclose(error,np.mean(np.abs(y[va]-search.predict(X[va]))))
            assert np.allclose(search.best_estimator_.named_steps['scale'].mean_,X[tr].mean(axis=0))
            for itr,iva in search.cv.split(X[tr]):
                assert not set(tr[itr])&set(tr[iva]) and not set(tr[itr])&set(va)
