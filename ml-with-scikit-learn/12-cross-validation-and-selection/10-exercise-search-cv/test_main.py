from solution import *

def test_01_behavior():
    """Exercise: search a bounded parameter space"""
    for n in [30,45]:
        X=np.arange(n*2,dtype=float).reshape(n,2); y=2*X[:,0]+np.sin(X[:,0])
        model=search_model(X,y)
        assert model is not None, 'Return the fitted search.'
        assert isinstance(model,GridSearchCV) and model.scoring=='neg_mean_absolute_error'
        assert model.param_grid=={'ridge__alpha':[0.1,1.0,10.0]} and model.n_jobs==1 and model.refit is True
        assert model.n_splits_==3 and len(model.cv_results_['params'])==3
        assert np.allclose(model.best_estimator_.named_steps['scale'].mean_,X.mean(axis=0))
        assert model.best_params_['ridge__alpha'] in [0.1,1.,10.]
