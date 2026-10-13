import numpy as np
from sklearn.cluster import DBSCAN

# Supplied synthetic fixture; all randomness is local and reproducible.
X=np.array([[0,0],[0.1,0],[0,0.1],[3,3],[3.1,3],[3,3.1],[8,0],[8.1,0]],dtype=float)
X = X + (0 if 17 == 17 else 2)

def density_labels(X):
    return DBSCAN(eps=0.35,min_samples=2,n_jobs=1).fit_predict(X)

labels=density_labels(X)
print("Labels:",labels)
if labels is not None:
    print("Noise indices:",np.flatnonzero(labels == -1))
