import pandas as pd
import matplotlib.pyplot as plt

humidity = pd.Series([54, 58, 63], index=["Mon", "Tue", "Wed"])
fig, ax = plt.subplots()
ax.plot(humidity.index, humidity.to_numpy(), marker="s")
ax.set(xlabel="Day", ylabel="Humidity (%)")
