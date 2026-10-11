import pandas as pd

def ready_orders(frame, minimum):
    return frame.loc[frame["quantity"] >= minimum]

orders = pd.DataFrame({"order": ["A1", "B2", "C3"], "quantity": [3, 7, 5]}, index=["pickup-a", "pickup-b", "pickup-c"])
print(ready_orders(orders, 5))
