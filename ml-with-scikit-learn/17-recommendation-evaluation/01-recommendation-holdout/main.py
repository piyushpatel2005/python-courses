from collections import defaultdict
import numpy as np
import pandas as pd

catalog = pd.read_json('catalog.json',orient='records',convert_dates=False,
                       dtype={'item_id':str,'available_since':str})
eligible_ids = set(catalog.loc[catalog['available_since'] <= '2025-01-19','item_id'])
event_table = pd.read_csv('interactions.csv',dtype=str,keep_default_na=False)
events = event_table.copy()

def chronological_holdout(events, eligible_ids):
    by_user=defaultdict(list)
    for event in events.itertuples(index=False,name=None):
        by_user[event[0]].append(event)
    result={'train':[],'validation':[],'test':[],'omitted':[]}
    for user in sorted(by_user):
        rows=sorted(by_user[user],key=lambda event:(event[2],event[1]))
        if len(rows)<4:
            result['omitted'].append(user)
            continue
        result['train'].extend(rows[:-2])
        result['validation'].append(rows[-2])
        result['test'].append(rows[-1])
    return result

result=chronological_holdout(events,eligible_ids)
print("Partitions:",result)
