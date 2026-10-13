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
    return None

training = pd.DataFrame({"size": [3., np.nan, 8., 10., 12., 15.], "material": ["ceramic", "metal", "ceramic", "metal", "ceramic", "metal"]})
target = np.array([18., 23., 30., 36., 38., 48.])
query = pd.DataFrame({"size": [6., np.nan], "material": ["metal", "silicone"]})

model = fit_prices(training, target)
print("Raw-row prices:", None if model is None else model.predict(query))
