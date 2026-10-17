import pandas as pd
import matplotlib.pyplot as plt

def plot_rain_visitors(frame):
    fig, ax = plt.subplots()
    return fig, ax

sample = pd.DataFrame({"rain_mm": [0, None, 12], "visitors": [32, 21, 15]})
fig, ax = plot_rain_visitors(sample)
