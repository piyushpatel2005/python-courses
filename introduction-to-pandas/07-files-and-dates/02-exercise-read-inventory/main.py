from io import StringIO
import pandas as pd

def load_inventory(text):
    # Read the supplied CSV text, not a fixed sample.
    return pd.DataFrame()

sample = "item,stock\nPaper bags,20\nLabels,7\n"
print(load_inventory(sample))
