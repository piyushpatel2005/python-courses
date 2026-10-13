from solution import *

def test_01_behavior():
    """Predict leaf means"""
    for scale in [1,3]:
        X=np.arange(8.).reshape(-1,1); y=np.array([1,3,8,10,20,22,35,37])*scale
        model=fit_tree(X,y)
        assert model is not None, 'Return a fitted regression tree.'
        assert isinstance(model,DecisionTreeRegressor) and model.max_depth==2
        leaves=model.apply(X)
        for leaf in np.unique(leaves):
            mask=leaves==leaf
            assert np.allclose(model.predict(X[mask]),np.mean(y[mask]))
        assert model.get_depth()==2
