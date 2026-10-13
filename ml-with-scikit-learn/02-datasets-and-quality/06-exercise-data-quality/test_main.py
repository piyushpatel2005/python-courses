from solution import *


def test_01_behavior():
    """Return a compact audit of missing cells duplicates invalid ranges and target imbalance without automatic deletion."""
    fixtures = [pd.DataFrame({"amount": [1., 2., 3., 4.], "label": [0, 0, 1, 0]}), pd.DataFrame({"amount": [np.nan, -2., 3., 3.], "label": [1, 0, 0, 0]}), pd.DataFrame({"amount": [-1., -4., np.nan, 7., 8.], "label": [1, 1, 1, 0, 0]})]
    for table in fixtures:
        before = table.copy(deep=True)
        got = audit(table)
        assert isinstance(got, dict), "Return the four audit measurements."
        expected = {"missing_fraction": table.isna().to_numpy().mean(), "duplicate_rows": table.duplicated().sum(), "invalid_amounts": (table.amount < 0).sum(), "positive_fraction": table.label.mean()}
        assert set(got) == set(expected)
        for key in expected:
            np.testing.assert_allclose(got[key], expected[key], rtol=1e-7, atol=1e-8, err_msg=key)
        pd.testing.assert_frame_equal(table, before)
