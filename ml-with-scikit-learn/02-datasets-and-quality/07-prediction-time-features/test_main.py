from solution import *


def test_01_behavior():
    """Select a feature schema available at prediction time and exclude IDs target proxies and post-outcome columns."""
    table = pd.DataFrame({"order_id": ["a", "b", "c"], "basket_value_usd": [11., 25., 63.], "item_count": [1, 2, 5], "actual_delivery_days": [2, 7, 4], "returned_30d": [0, 1, 1], "target_proxy": [0, 100, 100]}, index=[7, 3, 9])
    for amount in (11., 800.):
        changed = table.copy()
        changed.loc[7, "basket_value_usd"] = amount
        got = checkout_features(changed)
        assert isinstance(got, pd.DataFrame), "Return the selected DataFrame."
        pd.testing.assert_frame_equal(got, changed[["basket_value_usd", "item_count"]])
        changed["actual_delivery_days"] = [100, 200, 300]
        changed["returned_30d"] = [1, 0, 0]
        pd.testing.assert_frame_equal(checkout_features(changed), got)
