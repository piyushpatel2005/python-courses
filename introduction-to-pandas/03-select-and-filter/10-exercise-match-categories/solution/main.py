import pandas as pd

def invited(frame, types):
    return frame.loc[frame["type"].isin(types)]

sessions = pd.DataFrame({"session": ["Dye", "Seeds", "Baking"], "type": ["craft", "garden", "food"]}, index=["s4", "s5", "s6"])
print(invited(sessions, ["garden", "food"]))
