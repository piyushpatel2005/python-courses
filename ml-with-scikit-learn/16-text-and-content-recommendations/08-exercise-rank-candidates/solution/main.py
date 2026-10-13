import numpy as np

# Supplied synthetic fixture; all randomness is local and reproducible.
ids=['K08','K03','K05','K02','K07']
scores=[0.4,0.8,0.8,1.0,0.1]
seen={'K07'}
query_id='K02'

def rank_items(ids, scores, seen, query_id, k):
    blocked=set(seen)|{query_id}
    candidates=[(item,float(score)) for item,score in zip(ids,scores) if item not in blocked]
    return [item for item,score in sorted(candidates,key=lambda pair:(-pair[1],pair[0]))[:k]]

print("Eligible ranked IDs:",rank_items(ids,scores,seen,query_id,3))
