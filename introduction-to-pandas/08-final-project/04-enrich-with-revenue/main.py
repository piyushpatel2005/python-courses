from io import StringIO
import pandas as pd

SALES_CSV = (
    "sale_id,sold_at,stall_id,item,units,unit_price,channel\n"
    "1,2026-09-05,ST1,Apples,3,2.50,Walk-in\n"
    "2,2026-09-05,ST2,Bread,2,4.00,Preorder\n"
    "2,2026-09-05,ST2,Bread,2,4.00,Preorder\n"
    "3,2026-09-06,ST1,Apples,,2.50,Walk-in\n"
    "4,2026-09-06,ST3,Tea,1,3.00,Walk-in\n"
    "5,2026-09-07,ST2,Bread,4,4.00,Walk-in\n"
)
STALLS_CSV = (
    "stall_id,stall_name,neighborhood\n"
    "ST1,Orchard Table,North\n"
    "ST2,Oven Corner,South\n"
    "ST3,Tea Cart,North\n"
)

def read_tables(sales_text, stalls_text):
    # Task 1: Read sales.
    sales_frame = pd.read_csv(StringIO(sales_text))
    # Task 2: Read the directory.
    stalls_frame = pd.read_csv(StringIO(stalls_text))
    return sales_frame, stalls_frame

def clean_sales(sales):
    cleaned = sales.copy()
    # Task 1: Keep the first row for each sale ID.
    cleaned = cleaned.drop_duplicates(subset="sale_id")
    # Task 2: Parse dates; bad values become NaT.
    cleaned["sold_at"] = pd.to_datetime(cleaned["sold_at"], format="%Y-%m-%d", errors="coerce")
    # Task 3: Convert units.
    cleaned["units"] = pd.to_numeric(cleaned["units"], errors="coerce")
    # Task 4: Convert prices.
    cleaned["unit_price"] = pd.to_numeric(cleaned["unit_price"], errors="coerce")
    # Task 5: Remove rows without required values.
    cleaned = cleaned.dropna(subset=["sold_at", "units", "unit_price"])
    # Task 6: Keep amounts that belong in this sales report.
    cleaned = cleaned.loc[(cleaned["units"] > 0) & (cleaned["unit_price"] >= 0)]
    return cleaned.reset_index(drop=True)

def enrich_sales(cleaned):
    result = cleaned.copy()
    # Task 1: Add revenue.
    # Task 2: Add the day label.
    return result

sales, stalls = read_tables(SALES_CSV, STALLS_CSV)
print(enrich_sales(clean_sales(sales)))
