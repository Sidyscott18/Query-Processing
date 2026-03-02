import pandas as pd

df = pd.read_csv("sales_data.csv")

pivot = pd.pivot_table(df,
                       values='Sale_amt',
                       index=['Region','Manager','SalesMan'],
                       aggfunc='sum')

print(pivot)