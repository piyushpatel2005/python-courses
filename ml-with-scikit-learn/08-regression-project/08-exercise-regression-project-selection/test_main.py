from solution import *

def test_01_behavior():
    """Exercise: freeze one model setting"""
    parts = make_splits(make_data())
    train, val = parts["train"], parts["validation"]
    for candidates in ([0.1, 1., 10.], [12., 0.2]):
        result = choose_alpha(train, val, candidates)
        assert result is not None, "Return the selected alpha and validation errors."
        selected, errors = result
        expected = [mean_absolute_error(val.listed_price_usd, build_model(train[FEATURES], train.listed_price_usd, a).predict(val[FEATURES])) for a in candidates]
        assert np.allclose(errors, expected), "Only validation errors select alpha."
        assert selected == candidates[int(np.argmin(expected))]
        import solution
        saved_test = solution.parts["test"].copy(deep=True)
        try:
            solution.parts["test"].loc[:, "listed_price_usd"] = -99999.
            again = choose_alpha(train, val, candidates)
            assert selected == again[0] and np.allclose(errors, again[1]), "Sealed test changes cannot alter selection."
        finally:
            solution.parts["test"] = saved_test

