import pandas as pd
from  sklearn.preprocessing import MinMaxScaler,StandardScaler

df=pd.read_json("file.json")
print(df)
scaler=MinMaxScaler()

new_scaler=scaler.fit_transform(df)
print(new_scaler)