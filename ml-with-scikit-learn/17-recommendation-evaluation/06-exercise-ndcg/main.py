import numpy as np

# Supplied synthetic fixture; all randomness is local and reproducible.
ranked=['K08','K03','K09']
relevant={'K03','K09'}
k=3

def binary_ndcg(ranked, relevant, k):
    return None

print("NDCG at 3:",binary_ndcg(ranked,relevant,k))
