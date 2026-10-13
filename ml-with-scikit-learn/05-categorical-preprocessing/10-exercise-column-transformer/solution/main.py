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

training = pd.DataFrame({"volume_l": [2., 6., 10., 14.], "finish": ["matte", "gloss", "matte", "satin"], "product_id": ["K1", "K2", "K3", "K4"]})
numeric, category = "volume_l", "finish"

router = route_columns(training, numeric, category)
if router is not None:
    print("Feature names:", router.get_feature_names_out())
    print("Routed training rows:", router.transform(training))
else:
    print("Build the column router.")
