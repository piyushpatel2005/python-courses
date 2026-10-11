from io import StringIO
import pandas as pd

def load_roster(text):
    return pd.read_json(StringIO(text), orient="records")

sample = '[{"name":"Mara","shift":"morning"},{"name":"Luis","shift":"evening"}]'
print(load_roster(sample))
