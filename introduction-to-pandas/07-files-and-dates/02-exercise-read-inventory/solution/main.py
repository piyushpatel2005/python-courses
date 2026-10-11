from io import StringIO
import pandas as pd

def load_inventory(text):
    return pd.read_csv(StringIO(text))

sample = "item,stock\nPaper bags,20\nLabels,7\n"
print(load_inventory(sample))
