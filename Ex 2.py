import pandas as pd

df = pd.read_csv("job_history.csv")
result = df.groupby('EMPLOYEE_ID').filter(lambda x: len(x) >= 2)
print(result['EMPLOYEE_ID'].drop_duplicates())