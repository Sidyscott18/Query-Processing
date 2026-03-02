import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("alphabet_stock_data.csv", parse_dates=['Date'])

data = df[(df['Date'] >= '2016-10-03') & (df['Date'] <= '2016-10-07')]

plt.scatter(data['Volume'], data['Close'])
plt.xlabel("Volume")
plt.ylabel("Close Price")
plt.title("Volume vs Close Price")
plt.show()