import pandas as pd
import matplotlib.pyplot as plt

log = pd.DataFrame({"day": ["2024-06-01", "2024-06-03", "2024-06-08"], "trees": [12, 14, 17]})
dates = pd.to_datetime(log["day"])
fig, ax = plt.subplots()
ax.plot(dates, log["trees"], marker="s")
ax.set(xlabel="Date", ylabel="Watered trees (count)")
