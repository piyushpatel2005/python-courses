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
    return pd.read_csv("sample-parcels.csv", dtype={"product_id": str, "snapshot_date": str}, float_precision="round_trip")


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

def choose_alpha(train, validation, alphas=ALPHAS):
    errors = []
    for alpha in alphas:
        model = build_model(train[FEATURES], train["listed_price_usd"], alpha)
        predicted = model.predict(validation[FEATURES])
        errors.append(mean_absolute_error(validation["listed_price_usd"], predicted))
    return alphas[int(np.argmin(errors))], np.array(errors)

selection = choose_alpha(parts["train"], parts["validation"])
print("Frozen alpha and validation MAEs:", selection)

def final_report(train, validation, test, alpha):
    development = pd.concat([train, validation], axis=0)
    model = build_model(development[FEATURES], development["listed_price_usd"], alpha)
    predicted = model.predict(test[FEATURES])
    actual = test["listed_price_usd"].to_numpy()
    return {
        "model": model, "alpha": alpha,
        "development_ids": development.product_id.tolist(),
        "test_ids": test.product_id.tolist(),
        "n_development": len(development), "n_test": len(test),
        "predicted": predicted,
        "mae": mean_absolute_error(actual, predicted),
        "rmse": root_mean_squared_error(actual, predicted),
        "r2": r2_score(actual, predicted),
    }

report = final_report(parts["train"], parts["validation"], parts["test"], selection[0])
if report is None:
    print("Build the final report.")
else:
    for name in ("alpha", "n_development", "n_test", "mae", "rmse", "r2"):
        print(name, report[name])
    print("Synthetic same-population report; no optimal-pricing or future-demand claim.")

