import pandas as pd

def rename_seller(frame):
    return frame.rename(columns={"seller_name": "seller"})

def tidy_seller(frame):
    cleaned = frame.copy()
    cleaned["seller"] = cleaned["seller"].str.strip().str.lower()
    return cleaned

def convert_units(frame):
    cleaned = frame.copy()
    cleaned["units"] = pd.to_numeric(cleaned["units"], errors="coerce").astype("Int64")
    return cleaned

def drop_incomplete(frame):
    return frame.dropna(subset=["seller", "units"])

def fill_category(frame):
    return frame.fillna({"category": "unassigned"})

def keep_latest(frame):
    return frame.drop_duplicates(subset=["seller", "day"], keep="last")

def mark_ready(frame, minimum):
    cleaned = frame.copy()
    cleaned.loc[cleaned["units"] >= minimum, "status"] = "ready"
    return cleaned

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
        print(latest)
else:
    print(renamed)
