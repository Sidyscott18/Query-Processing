import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("alphabet_stock_data.csv", parse_dates=['Date'])
data = df[(df['Date'] >= '2016-10-03') & (df['Date'] <= '2016-10-07')]

plt.plot(data['Date'], data['Close'])
plt.xlabel("Date")
plt.ylabel("Close Price")
plt.title("Alphabet Stock Price")
plt.show()