from solution import *
import pandas as pd

def test_vendor_series():
    """Extract the vendor Series on changing rosters"""
    for values in [["Mina", "Sol"], ["Ash", "Jo", "Lee"]]:
        frame = pd.DataFrame({"vendor": values, "phone": list(range(len(values))), "booth": list(range(len(values)))}, index=[f"v{i}" for i in range(len(values))])
        for limit in [0, 1, 2, 5]:
            pd.testing.assert_series_equal(vendor_names(frame, limit), frame["vendor"].head(limit))

def test_contact_sheet():
    """Preserve rows, index, and the two requested columns"""
    for vendors in [["Mina", "Sol"], ["Ash", "Jo", "Lee"]]:
        frame = pd.DataFrame({"phone": range(len(vendors)), "vendor": vendors, "booth": range(len(vendors))}, index=[f"v{i}" for i in range(len(vendors))])
        for limit in [0, 1, 2, 5]:
            pd.testing.assert_frame_equal(contact_sheet(frame, limit), frame[["vendor", "phone"]].tail(limit))
