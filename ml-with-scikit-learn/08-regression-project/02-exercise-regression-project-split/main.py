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
    return None

parts = make_splits(make_data())
print("Partition sizes:", None if parts is None else {k: len(v) for k, v in parts.items()})

