import numpy as np
from scipy.sparse import csr_matrix
from sklearn.metrics.pairwise import cosine_similarity

# Supplied synthetic fixture; all randomness is local and reproducible.
ids=['K01','K02','K03','K04','K05']
item_matrix=csr_matrix([[0,2,0],[0,0,2],[0,1,1],[2,0,0],[1,1,0]])
history=['K02','K03']

def mean_profile(ids, item_matrix, history):
    lookup={item:i for i,item in enumerate(ids)}
    rows=[lookup[item] for item in sorted(set(history)) if item in lookup]
    if not rows:
        return np.zeros((1,item_matrix.shape[1]))
    return np.asarray(item_matrix[rows].mean(axis=0))

profile=mean_profile(ids,item_matrix,history)
print("Training-history mean:",profile)
if profile is not None:
    scores=cosine_similarity(profile,item_matrix).ravel()
    eligible=[(item,float(score)) for item,score in zip(ids,scores) if item not in history]
    print("Unseen ranking:",sorted(eligible,key=lambda pair:(-pair[1],pair[0])))
