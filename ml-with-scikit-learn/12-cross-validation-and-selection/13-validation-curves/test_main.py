from solution import *

def test_01_behavior():
    """Vary one model setting"""
    for n in [30,42]:
        rng=np.random.default_rng(n); X=rng.normal(size=(n,2)); y=X[:,0]+rng.normal(size=n)
        result=alpha_curve(X,y)
        assert result is not None, 'Return alpha values and errors.'
        alphas,train,valid=result
        assert np.array_equal(alphas,[0.1,1.,10.]) and train.shape==valid.shape==(3,3)
        expected=validation_curve(Pipeline([('impute',SimpleImputer(strategy='median')),('scale',StandardScaler()),('ridge',Ridge())]),X,y,param_name='ridge__alpha',param_range=[0.1,1.,10.],cv=KFold(3,shuffle=True,random_state=17),scoring='neg_mean_absolute_error',n_jobs=1)
        assert np.allclose(train,-expected[0]) and np.allclose(valid,-expected[1])
