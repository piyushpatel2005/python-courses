from solution import *

def test_01_analogue():
    """Report final classification errors"""
    from types import SimpleNamespace
    test=pd.DataFrame({'weight_kg':[0.1,0.3,0.7,0.9,0.2], 'width_cm':1., 'material':'wood', 'flagged':[0,1,1,1,0]})
    model=SimpleNamespace(classes_=np.array([0,1]),named_steps={'logistic':SimpleNamespace(C=2.)},predict_proba=lambda X:np.column_stack([1-X.weight_kg,X.weight_kg]))
    for threshold in [0.25,0.75]:
        result=final_report(model,threshold,test)
        assert np.array_equal(result['confusion_matrix'],confusion_matrix(test.flagged,test.weight_kg>=threshold,labels=[0,1])), 'Rows and columns must use [0, 1].'
