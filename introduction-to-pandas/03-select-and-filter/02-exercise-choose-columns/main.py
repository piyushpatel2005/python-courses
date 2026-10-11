import pandas as pd

def vendor_names(frame, limit):
    return pd.Series(dtype="object")

def contact_sheet(frame, limit):
    return frame.iloc[:, :0].copy()

vendors = pd.DataFrame({"vendor": ["Mina", "Sol"], "phone": ["555-0181", "555-0182"], "booth": [4, 7]})
print(vendor_names(vendors, 1))
print(contact_sheet(vendors, 1))
