import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import csr_matrix

# Supplied synthetic fixture; all randomness is local and reproducible.
items=csr_matrix([[0,3,0],[1,0,1],[0,0,0],[0,1,1]])
queries=csr_matrix([[0,6,0],[1,0,1]])

def compare_vectors(queries, items):
    return None

print("Query-by-item similarities:",compare_vectors(queries,items))
