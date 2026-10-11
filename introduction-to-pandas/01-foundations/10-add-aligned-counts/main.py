import pandas as pd

morning = pd.Series([4, 7], index=["north", "south"])
afternoon = pd.Series([3, 2], index=["south", "north"])
total = morning + afternoon
print(total)
