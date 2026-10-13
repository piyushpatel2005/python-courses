from collections import defaultdict
import numpy as np
import pandas as pd

catalog = pd.read_json('catalog.json',orient='records',convert_dates=False,
                       dtype={'item_id':str,'available_since':str})
eligible_ids = set(catalog.loc[catalog['available_since'] <= '2025-01-19','item_id'])
event_table = pd.read_csv('interactions.csv',dtype=str,keep_default_na=False)
events = event_table.copy()

def chronological_holdout(events, eligible_ids):
    return None

result=chronological_holdout(events,eligible_ids)
print("Partitions:",result)
