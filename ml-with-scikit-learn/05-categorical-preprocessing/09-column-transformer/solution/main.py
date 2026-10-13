import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder


def route_columns(training, numeric, category):
    router = ColumnTransformer([
        ("numeric", StandardScaler(), [numeric]),
        ("category", OneHotEncoder(sparse_output=False, handle_unknown="ignore"), [category]),
    ], remainder="drop", n_jobs=1)
    return router.fit(training)

training = pd.DataFrame({"weight_kg": [1., 2., 4., 5.], "material": ["wood", "steel", "wood", "glass"], "product_id": ["A", "B", "C", "D"]})
numeric, category = "weight_kg", "material"

router = route_columns(training, numeric, category)
if router is not None:
    print("Feature names:", router.get_feature_names_out())
    print("Routed training rows:", router.transform(training))
else:
    print("Build the column router.")
