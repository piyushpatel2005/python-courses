import pandas as pd

def invited(frame, types):
    return frame.iloc[:0].copy()

sessions = pd.DataFrame({"session": ["Dye", "Seeds", "Baking"], "type": ["craft", "garden", "food"]}, index=["s4", "s5", "s6"])
print(invited(sessions, ["garden", "food"]))
