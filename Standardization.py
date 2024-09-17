import pandas as pd 
from sklearn.preprocessing import StandardScaler
file_path=r'C:\Users\ADMIN\OneDrive\Desktop\AIML githup\Normalization-and-standardization\file.csv'
df=pd.read_csv(file_path)
scaler=StandardScaler()
df["new_project_name"]=scaler.fit_transform(df[["Duration"]])
print(df)