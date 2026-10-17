import pandas as pd
import matplotlib.pyplot as plt

returns = pd.DataFrame({"day": pd.date_range("2024-04-01", periods=8), "books": [8, 11, 9, 14, 10, 13, 15, 12]})
fig, ax = plt.subplots()
ax.plot(returns["day"], returns["books"], marker="o")
ax.tick_params(axis="x", labelrotation=45)
ax.set(xlabel="Date", ylabel="Returns (books)")
