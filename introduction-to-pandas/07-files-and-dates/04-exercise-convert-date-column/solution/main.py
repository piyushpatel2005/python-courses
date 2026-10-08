import pandas as pd

def convert_signups(frame):
    result = frame.copy()
    result["signed_on"] = pd.to_datetime(result["signed_on"])
    return result

sample = pd.DataFrame({"signed_on": ["2026-09-03", "2026-09-04"], "volunteer": ["Ada", "Bo"]})
print(convert_signups(sample).dtypes)
