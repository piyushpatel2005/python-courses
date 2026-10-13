import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LinearRegression

def preprocessor():
    numeric = Pipeline([("fill", SimpleImputer(strategy="median")), ("scale", StandardScaler())])
    categorical = Pipeline([("fill", SimpleImputer(strategy="most_frequent")), ("encode", OneHotEncoder(sparse_output=False, handle_unknown="ignore"))])
    return ColumnTransformer([("numeric", numeric, ["size"]), ("category", categorical, ["material"])], n_jobs=1)

def fit_prices(training, target):
    model = Pipeline([("prepare", preprocessor()), ("model", LinearRegression(n_jobs=1))])
    return model.fit(training.fillna({"size": 0.}), target)

training = pd.DataFrame({"size": [1., 2., np.nan, 5., 7., 9.], "material": ["wood", "steel", "wood", "steel", "wood", "steel"]})
target = np.array([14., 19., 21., 29., 31., 42.])
query = pd.DataFrame({"size": [np.nan, 10.], "material": ["wood", "glass"]})

model = fit_prices(training, target)
print("Raw-row prices:", None if model is None else model.predict(query))
