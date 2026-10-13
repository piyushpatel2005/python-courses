from solution import *

def test_01_behavior():
    """Exercise: average randomized trees"""
    for shift in [0,12]:
        X=np.arange(12.).reshape(-1,1); y=np.sin(X[:,0])+shift
        model=fit_forest(X,y)
        assert model is not None, 'Return the fitted forest.'
        assert isinstance(model,RandomForestRegressor)
        assert len(model.estimators_)==10 and model.max_depth==3 and model.n_jobs==1 and model.random_state==17
        Q=np.array([[1.5],[7.5],[14.]])
        assert np.allclose(model.predict(Q),np.mean([tree.predict(Q) for tree in model.estimators_],axis=0))
        assert np.allclose(model.predict(Q),fit_forest(X,y).predict(Q))
