from solution import *

def test_01_behavior():
    """Exercise: add trees to correct errors"""
    for offset in [0,4]:
        X=np.arange(12.).reshape(-1,1); y=X[:,0]**2+offset
        model=fit_boosting(X,y)
        assert model is not None, 'Return fitted boosting.'
        assert isinstance(model,GradientBoostingRegressor) and model.n_estimators==15
        assert model.learning_rate==0.1 and model.max_depth==2 and model.random_state==17
        stages=list(model.staged_predict(X))
        assert len(stages)==15 and np.allclose(stages[-1],model.predict(X))
        first=model.init_.predict(X)+model.learning_rate*model.estimators_[0,0].predict(X)
        assert np.allclose(stages[0],first)
