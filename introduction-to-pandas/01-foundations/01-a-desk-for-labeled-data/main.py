import pandas as pd

# Each count sits beside a stall label.
counts = pd.Series([8, 5], index=["bread", "flowers"])
print(counts)
