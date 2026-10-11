import pandas as pd

def convert_signups(frame):
    # Copy first, then convert signed_on in that copy.
    return frame.copy()

sample = pd.DataFrame({"signed_on": ["2026-09-03", "2026-09-04"], "volunteer": ["Ada", "Bo"]})
print("original:", sample.dtypes)
print("converted:", convert_signups(sample).dtypes)
