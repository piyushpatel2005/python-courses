from solution import *

def test_01_behavior():
    """Trace a decision tree"""
    for offset in [0,10]:
        X=np.arange(9,dtype=float).reshape(-1,1)+offset; y=np.repeat([0,1,2],3)
        model=fit_tree(X,y)
        assert model is not None, 'Return a fitted tree.'
        assert isinstance(model,DecisionTreeClassifier) and model.max_depth==2
        assert model.random_state==17 and np.array_equal(model.predict(X),y)
        leaves=model.apply(X)
        for leaf in np.unique(leaves):
            members=y[leaves==leaf]
            expected=np.bincount(members).argmax()
            assert np.all(model.predict(X[leaves==leaf])==expected)
