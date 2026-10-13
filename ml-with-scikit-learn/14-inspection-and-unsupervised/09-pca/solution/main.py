import numpy as np
from sklearn.decomposition import PCA
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split

# Supplied external digits benchmark; the split is reproducible.
X = load_digits().data[:240]
X_train,X_valid = train_test_split(X,test_size=0.25,random_state=17)

def fit_projection(X):
    return PCA(n_components=2, svd_solver='full').fit(X)

model = fit_projection(X_train)
if model is not None:
    reduced = model.transform(X_valid)
    print("Validation reduced shape:",reduced.shape)
    print("Retained variance:",model.explained_variance_ratio_.sum())
    print("Reconstruction shape:",model.inverse_transform(reduced).shape)
