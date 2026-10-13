import numpy as np
from sklearn.cluster import KMeans
import pandas as pd

table = pd.read_csv('product-measurements.csv')
X = table[['width_index', 'depth_index']]

def fit_clusters(X):
    return None

model=fit_clusters(X)
if model is not None:
    print("Centers:",model.cluster_centers_)
    print("Cluster counts:",np.bincount(model.labels_))
    print("Inertia:",model.inertia_)
