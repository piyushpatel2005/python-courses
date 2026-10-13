import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyRegressor
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error, root_mean_squared_error, r2_score

FEATURES = ["weight_kg", "volume_l", "material_cost_usd"]
ALPHAS = [0.1, 1.0, 10.0]

def make_data():
    """Read the fixed synthetic 2025-01-15 snapshot."""
    return pd.read_csv("listing-prices.csv", dtype={"product_id": str, "snapshot_date": str}, float_precision="round_trip")


def make_splits(table):
    development, test = train_test_split(table, test_size=0.2, random_state=41)
    train, validation = train_test_split(development, test_size=0.25, random_state=41)
    return {"train": train.copy(), "validation": validation.copy(), "test": test.copy()}

parts = make_splits(make_data())
print("Partition sizes:", None if parts is None else {k: len(v) for k, v in parts.items()})

def baseline_mae(train, validation):
    baseline = DummyRegressor(strategy="mean")
    baseline.fit(np.zeros((len(train), 1)), train["listed_price_usd"])
    predicted = baseline.predict(np.zeros((len(validation), 1)))
    return mean_absolute_error(validation["listed_price_usd"], predicted)

print("Training-mean baseline validation MAE:", baseline_mae(parts["train"], parts["validation"]))

def build_model(training, target, alpha=1.0):
    model = Pipeline([
        ("impute", SimpleImputer(strategy="median")),
        ("scale", StandardScaler()),
        ("ridge", Ridge(alpha=alpha)),
    ])
    return model.fit(training, target)

model = build_model(parts["train"][FEATURES], parts["train"].listed_price_usd)
print("Pipeline validation MAE:", None if model is None else mean_absolute_error(parts["validation"].listed_price_usd, model.predict(parts["validation"][FEATURES])))

