import pandas as pd
import matplotlib.pyplot as plt

counts = pd.DataFrame({"day": [3, 1, 2], "volunteers": [9, 4, 7]})
ordered = counts.sort_values("day")
fig, ax = plt.subplots()
ax.plot(ordered["day"], ordered["volunteers"], color="purple", marker="o")
ax.set(xlabel="Day", ylabel="Volunteers (people)")
