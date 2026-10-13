from solution import *

def test_01_analogue():
    """Assemble a mixed-feature classifier"""
    data=make_analogue(); model=build_model().fit(data[FEATURES],data.flagged)
    query=pd.DataFrame({'weight_kg':[np.nan,2.], 'width_cm':[30.,np.nan], 'material':['glass','wood']})
    assert np.isfinite(model.predict_proba(query)).all(), 'Ignore unknown material categories.'
