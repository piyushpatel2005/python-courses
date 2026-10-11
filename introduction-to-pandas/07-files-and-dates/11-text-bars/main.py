import pandas as pd

def visit_bars(counts, scale=2):
    return "\n".join(f"{name}: {'#' * (int(count) * scale)}" for name, count in counts.items())

sample = pd.Series([3, 1], index=["Garden", "Kitchen"])
print(visit_bars(sample))
