import pandas as pd

df = pd.read_csv("departments.csv")
print(df['DEPARTMENT_ID'].drop_duplicates())