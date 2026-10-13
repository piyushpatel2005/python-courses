import numpy as np
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, cross_val_score
import pandas as pd

table = pd.read_csv('checkout-measurements.csv')
X = table[['basket_index', 'item_count_index', 'category_index', 'season_index']]
y = table['returned']
X_train, X_valid, y_train, y_valid = train_test_split(
    X, y, test_size=0.25, stratify=y, random_state=17)

def fit_selected(X, y):
    return Pipeline([('select', SelectKBest(f_classif, k=1)),
                     ('model', LogisticRegression(max_iter=300, n_jobs=1))]).fit(X,y)

model = fit_selected(X_train,y_train)
if model is not None:
    print("Selected columns:", model.named_steps['select'].get_support())
    print("Training-only CV:", cross_val_score(model,X_train,y_train,cv=3,n_jobs=1))
    print("Validation accuracy:", model.score(X_valid,y_valid))
