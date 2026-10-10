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
    sales_frame = pd.DataFrame()
    # Task 2: Read the directory.
    stalls_frame = pd.DataFrame()
    return sales_frame, stalls_frame

sales, stalls = read_tables(SALES_CSV, STALLS_CSV)
print("sales rows:", len(sales), "stalls:", len(stalls))
