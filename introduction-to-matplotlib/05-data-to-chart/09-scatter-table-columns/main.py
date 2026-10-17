import pandas as pd
import matplotlib.pyplot as plt

beds = pd.DataFrame({"shade_hours": [2, 5, 3], "height_cm": [12, 8, 10]})
fig, ax = plt.subplots()
ax.scatter(beds["shade_hours"], beds["height_cm"], s=40)
ax.set(xlabel="Shade (hours)", ylabel="Height (cm)")
