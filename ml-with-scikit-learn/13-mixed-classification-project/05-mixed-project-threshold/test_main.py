from solution import *

def test_01_analogue():
    """Set an operational threshold"""
    from types import SimpleNamespace
    for scores in [[0.25,0.1],[0.5,0.2],[0.75,0.1]]:
        validation=pd.DataFrame({'weight_kg':scores,'width_cm':1.,'material':'wood','flagged':[1,0]})
        model=SimpleNamespace(classes_=np.array([0,1]),predict_proba=lambda X:np.column_stack([1-X.weight_kg,X.weight_kg]))
        assert choose_threshold(model,validation)==scores[0], 'Include scores exactly on the threshold.'
