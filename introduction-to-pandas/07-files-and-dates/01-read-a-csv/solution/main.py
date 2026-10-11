from io import StringIO
import pandas as pd

def load_visits(text):
    return pd.read_csv(StringIO(text), sep=",")

sample = "stall,visits\nFlower Cart,8\nSoup Stand,5\n"
print(load_visits(sample))
