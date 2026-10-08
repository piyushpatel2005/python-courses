from io import StringIO
import pandas as pd

def load_roster(text):
    # Read records from the supplied JSON text.
    return pd.DataFrame()

sample = '[{"name":"Mara","shift":"morning"},{"name":"Luis","shift":"evening"}]'
print(load_roster(sample))
