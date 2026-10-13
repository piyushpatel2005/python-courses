import numpy as np
from sklearn.metrics import silhouette_score
import pandas as pd

table = pd.read_csv('product-measurements.csv')
X = table[['width_index', 'depth_index']]
labels = table['group_label']

def safe_silhouette(X, labels):
    return None

print("Two-group silhouette:",safe_silhouette(X,labels))
print("One-group result:",safe_silhouette(X,np.zeros(len(X))))
