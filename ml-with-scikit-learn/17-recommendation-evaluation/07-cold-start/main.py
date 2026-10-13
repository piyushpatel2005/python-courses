from collections import Counter
import numpy as np
import pandas as pd

catalog = pd.read_json('catalog.json',orient='records',convert_dates=False,
                       dtype={'item_id':str,'available_since':str})
ids = catalog['item_id'].iloc[::-1].tolist()
views = pd.read_csv('training-views.csv',dtype=str)
training_events = views[['user_id','item_id']].copy()
seen = {ids[-1]}

def popular_items(ids, training_events, seen, k):
    counts=Counter(training_events['item_id'])
    return sorted((item for item in ids if item not in seen),
                  key=lambda item:-counts[item])[:k]

ranked=popular_items(ids,training_events,seen,3)
print("Cold-user fallback:",ranked)
if ranked is not None:
    print("This list's catalog coverage:",len(set(ranked))/len(ids))
