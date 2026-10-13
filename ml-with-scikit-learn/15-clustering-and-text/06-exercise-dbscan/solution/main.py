import numpy as np
from sklearn.cluster import DBSCAN

# Supplied synthetic fixture; all randomness is local and reproducible.
X = np.array([[-3,0],[-2.9,0],[-3,0.1],
              [0,3],[0.1,3],[0,3.1],
              [3,-2],[3.1,-2],[3,-1.9],
              [8,4],[8.1,4]], dtype=float)

def density_labels(X):
    return DBSCAN(eps=0.35,min_samples=3,n_jobs=1).fit_predict(X)

labels=density_labels(X)
print("Labels:",labels)
if labels is not None:
    print("Noise indices:",np.flatnonzero(labels == -1))
