import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.utils.class_weight import compute_class_weight
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
import pandas as pd

table = pd.read_csv('checkout-measurements.csv')
X = table[['basket_index', 'item_count_index']]
y = table['returned']
X_train, X_valid, y_train, y_valid = train_test_split(
    X, y, test_size=0.3, stratify=y, random_state=29)

def fit_weighted(X, y):
    return LogisticRegression(class_weight="balanced", max_iter=300,
                                  n_jobs=1).fit(X, y)

model = fit_weighted(X_train, y_train)
print("Training weights:", compute_class_weight('balanced', classes=np.unique(y_train), y=y_train))
print("Validation prevalence:", y_valid.mean())
print("Unweighted confusion:", confusion_matrix(y_valid, LogisticRegression(n_jobs=1).fit(X_train, y_train).predict(X_valid)))
if model is not None:
    print("Weighted confusion:", confusion_matrix(y_valid, model.predict(X_valid)))
