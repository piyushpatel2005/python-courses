import numpy as np
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
import pandas as pd

table = pd.read_csv('product-measurements.csv')
X = table[['width_index', 'depth_index', 'height_index']]
X_train, X_valid = train_test_split(X,test_size=0.25,random_state=29)

def fit_projection(X):
    return PCA(n_components=2, svd_solver='full').fit(X)

model = fit_projection(X_train)
if model is not None:
    reduced = model.transform(X_valid)
    print("Validation reduced shape:",reduced.shape)
    print("Retained variance:",model.explained_variance_ratio_.sum())
    print("Reconstruction shape:",model.inverse_transform(reduced).shape)
