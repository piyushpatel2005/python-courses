from solution import *

def test_01_behavior():
    """Vary the amount of training data"""
    for n in [36,60]:
        rng=np.random.default_rng(n); X=rng.normal(size=(n,2)); y=X[:,0]+rng.normal(size=n)
        result=size_curve(X,y)
        assert result is not None, 'Return sizes and both error matrices.'
        sizes,train,valid=result
        assert np.array_equal(sizes,(np.array([0.5,0.75,1.])*(n*2//3)).astype(int))
        assert train.shape==valid.shape==(3,3) and np.all(train>=0) and np.all(valid>=0)
        expected=learning_curve(Pipeline([('impute',SimpleImputer(strategy='median')),('scale',StandardScaler()),('ridge',Ridge())]),X,y,train_sizes=[0.5,0.75,1.],cv=KFold(3,shuffle=True,random_state=17),scoring='neg_mean_absolute_error',n_jobs=1,shuffle=True,random_state=17)
        assert np.allclose(train,-expected[1]) and np.allclose(valid,-expected[2])
