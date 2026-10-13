from solution import *

def test_01_behavior():
    """Exercise: use stratified classification folds"""
    from sklearn.metrics import f1_score as expected_f1
    for seed in [12,23]:
        rng=np.random.default_rng(seed); X=rng.normal(size=(45,2)); y=np.array([0]*30+[1]*15)
        result=evaluate_classes(X,y)
        assert result is not None, 'Return folds, scores, and models.'
        folds,scores,models=result
        expected=list(StratifiedKFold(3,shuffle=True,random_state=17).split(X,y))
        assert len(folds)==3
        for (tr,va),(etr,eva),score,model in zip(folds,expected,scores,models):
            assert np.array_equal(tr,etr) and np.array_equal(va,eva)
            assert set(y[va])=={0,1} and not set(tr)&set(va)
            assert np.isclose(score,expected_f1(y[va],model.predict(X[va]),average='macro'))
            assert np.allclose(model.named_steps['scale'].mean_,X[tr].mean(axis=0))
