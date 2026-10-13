from solution import *

def test_01_behavior():
    """Exercise: record a regression baseline"""
    for values in ([10., 20., 30.], [40., 50., 90.]):
        train = pd.DataFrame({"listed_price_usd": values})
        val = pd.DataFrame({"listed_price_usd": [5., 15., 20., 120.]})
        got = baseline_mae(train, val)
        assert got is not None, "Return validation MAE."
        expected = np.mean(np.abs(val.listed_price_usd.to_numpy()-np.mean(values)))
        assert np.isclose(got, expected), "Fit the baseline mean on training prices only."

