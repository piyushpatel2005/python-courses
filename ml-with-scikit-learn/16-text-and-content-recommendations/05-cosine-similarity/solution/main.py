import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import csr_matrix

# Supplied synthetic fixture; all randomness is local and reproducible.
items=csr_matrix([[1,0],[0,1],[1,1],[0,0]])
queries=csr_matrix([[2,0],[0,0]])

def compare_vectors(queries, items):
    return cosine_similarity(queries,items)

print("Query-by-item similarities:",compare_vectors(queries,items))
