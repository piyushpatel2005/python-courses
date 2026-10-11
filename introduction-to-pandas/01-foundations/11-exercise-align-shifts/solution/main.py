import pandas as pd

def combine_shifts(first, second):
    return first + second

print(combine_shifts(pd.Series([3, 5], index=["tea", "jam"]), pd.Series([4, 2], index=["jam", "tea"])))
