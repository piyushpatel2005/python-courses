import numpy as np

# Supplied synthetic fixture; all randomness is local and reproducible.
ranked=['F04','F02','F05']
relevant={'F02'}
k=3

def binary_ndcg(ranked, relevant, k):
    relevant=set(relevant)
    if not relevant:
        return 0.0
    return len(set(ranked[:k]) & relevant)/min(k,len(relevant))

print("NDCG at 3:",binary_ndcg(ranked,relevant,k))
