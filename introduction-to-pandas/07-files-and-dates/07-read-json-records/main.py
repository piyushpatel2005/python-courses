from io import StringIO
import pandas as pd

def lookup_names(text):
    frame = pd.read_json(StringIO(text), orient="records")
    return frame["stall_id"]

sample = '[{"stall_id":"S1","name":"Honey Table"},{"stall_id":"S2","name":"Clay Corner"}]'
print(lookup_names(sample).tolist())
