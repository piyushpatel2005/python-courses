from solution import *
import pandas as pd

def test_missing_addresses():
    """Identify missing address cells on changing rows"""
    for addresses in [["North gate", None, "Main hall"], [None, "Side door", "", "Office"]]:
        frame = pd.DataFrame({"address": addresses, "phone": [None] * len(addresses)}, index=[f"d{i}" for i in range(len(addresses))])
        pd.testing.assert_series_equal(missing_addresses(frame), frame["address"].isna())

def test_routable():
    """Require an address, not a phone"""
    for addresses in [["North gate", None, "Main hall"], [None, "Side door", "", "Office"]]:
        frame = pd.DataFrame({"address": addresses, "phone": [None] * len(addresses)}, index=[f"d{i}" for i in range(len(addresses))])
        pd.testing.assert_frame_equal(routable(frame), frame.dropna(subset=["address"]))
