import pandas as pd

def label_window(frame, start, stop):
    return frame.loc[start:stop, ["item", "count"]]

def position_window(frame, start, stop):
    return frame.iloc[start:stop, 0:2]

deliveries = pd.DataFrame({"item": ["Apples", "Beans", "Bread"], "count": [6, 10, 8], "dock": ["A", "B", "A"]}, index=["dawn", "noon", "night"])
print(label_window(deliveries, "dawn", "noon"))
print(position_window(deliveries, 1, 3))
