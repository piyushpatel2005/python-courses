import pandas as pd

def rename_seller(frame):
    return frame.copy()

def tidy_seller(frame):
    return frame.copy()

def convert_units(frame):
    return frame.copy()

def drop_incomplete(frame):
    return frame.copy()

def fill_category(frame):
    return frame.copy()

def keep_latest(frame):
    return frame.copy()

def mark_ready(frame, minimum):
    return frame.copy()

raw = pd.DataFrame({
    "seller_name": ["  MINA ", "Mina", " Sol "],
    "day": ["Fri", "Fri", "Sat"],
    "units": ["4", "7", "unknown"],
    "category": [None, "veg", "bread"],
    "status": ["pending", "pending", "pending"],
}, index=["first", "revised", "unusable"])
renamed = rename_seller(raw)
if "seller" in renamed.columns:
    tidied = tidy_seller(renamed)
    converted = convert_units(tidied)
    complete = drop_incomplete(converted)
    categorized = fill_category(complete)
    latest = keep_latest(categorized)
    if pd.api.types.is_numeric_dtype(latest["units"]):
        print(mark_ready(latest, 6))
    else:
        print(latest)  # The quantity conversion is still being built.
else:
    print(renamed)  # Start here; the remaining steps run after the rename works.
