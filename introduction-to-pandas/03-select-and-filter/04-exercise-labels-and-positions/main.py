import pandas as pd

def label_window(frame, start, stop):
    return frame.iloc[:0].copy()

def position_window(frame, start, stop):
    return frame.iloc[:0].copy()

deliveries = pd.DataFrame({"item": ["Apples", "Beans", "Bread"], "count": [6, 10, 8], "dock": ["A", "B", "A"]}, index=["dawn", "noon", "night"])
print(label_window(deliveries, "dawn", "noon"))
print(position_window(deliveries, 1, 3))
