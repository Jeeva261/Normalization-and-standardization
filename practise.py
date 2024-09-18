# 1.Normalize a dataset using Min-Max scaling.
# 2.Standardize a dataset using Z-score.

import pandas as pd
from sklearn.preprocessing import MinMaxScaler,StandardScaler

df=pd.read_json("opendata.json")
scaler_value=MinMaxScaler().fit_transform(df)
print(scaler_value)

df=pd.read_csv("dirtydata.csv")
fscaler_value=StandardScaler().fit_transform(df[["Pulse"]])
print(fscaler_value)
