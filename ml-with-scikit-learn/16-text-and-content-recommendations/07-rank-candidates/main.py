import numpy as np

# Supplied synthetic fixture; all randomness is local and reproducible.
ids=['F04','F02','F01','F03']
scores=[0.7,0.7,1.0,0.2]
seen={'F03'}
query_id='F01'

def rank_items(ids, scores, seen, query_id, k):
    blocked=set(seen)|{query_id}
    candidates=[(item,float(score)) for item,score in zip(ids,scores) if item not in blocked]
    return [item for item,score in sorted(candidates,key=lambda pair:-pair[1])[:k]]

print("Eligible ranked IDs:",rank_items(ids,scores,seen,query_id,3))
