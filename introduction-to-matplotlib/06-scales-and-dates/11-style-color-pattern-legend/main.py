import matplotlib.pyplot as plt

with plt.style.context("ggplot"):
    fig, ax = plt.subplots(constrained_layout=True)
    ax.plot([1, 2, 3], [9, 12, 16], color="#0072B2", linestyle="-", label="North pickup")
    ax.plot([1, 2, 3], [7, 13, 15], color="#D55E00", linestyle="-", label="South pickup")
    ax.set(xlabel="Week", ylabel="Collections (bags)")
    ax.legend()
