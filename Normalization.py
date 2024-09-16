import  pandas as pd
from sklearn.preprocessing import MinMaxScaler

file_path = 'C:/Users/ADMIN/OneDrive/Desktop/AIML_github/Normalization-and-standardization/file.json'
df=pd.read_json(file_path)
print(df)
scaler=MinMaxScaler()
new_scaler=scaler.fit_transform(df)
print(new_scaler)