from solution import *

def test_01_behavior():
    """Evaluate the frozen regression model"""
    parts = make_splits(make_data())
    train, val, test = parts["train"], parts["validation"], parts["test"]
    for alpha in (0.1, 10.):
        got = final_report(train, val, test, alpha)
        assert isinstance(got, dict), "Return the final report dictionary."
        dev = pd.concat([train, val], axis=0)
        reference = build_model(dev[FEATURES], dev.listed_price_usd, alpha)
        expected = reference.predict(test[FEATURES])
        assert got["development_ids"] == dev.product_id.tolist()
        assert got["test_ids"] == test.product_id.tolist()
        assert got["n_development"] == len(dev) and got["n_test"] == len(test)
        assert got["alpha"] == alpha
        assert got["model"].named_steps["scale"].n_samples_seen_ == len(dev)
        assert np.allclose(got["predicted"], expected)
        y = test.listed_price_usd
        assert np.isclose(got["mae"], mean_absolute_error(y, expected))
        assert np.isclose(got["rmse"], root_mean_squared_error(y, expected))
        assert np.isclose(got["r2"], r2_score(y, expected))
        changed = test.copy(); changed.loc[:, "listed_price_usd"] += 1000.
        again = final_report(train, val, changed, alpha)
        assert np.allclose(again["predicted"], got["predicted"]), "Test labels may change metrics but never the fitted model."
        assert np.allclose(again["model"].named_steps["impute"].statistics_, got["model"].named_steps["impute"].statistics_)

