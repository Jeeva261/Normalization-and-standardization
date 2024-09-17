import pandas as pd
from sklearn.preprocessing import MinMaxScaler
file_path=r'C:\Users\ADMIN\OneDrive\Desktop\AIML githup\Normalization-and-standardization\file.csv'
df=pd.read_csv(file_path)
scaler=MinMaxScaler()
df["new_scaler"]=scaler.fit_transform(df[["Duration"]])
print(df)






