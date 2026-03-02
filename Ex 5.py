import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("alphabet_stock_data.csv", parse_dates=['Date'])

# Filter between two dates (modify if needed)
data = df[(df['Date'] >= '2016-10-03') & (df['Date'] <= '2016-10-07')]

plt.bar(data['Date'], data['Volume'])
plt.xlabel("Date")
plt.ylabel("Volume")
plt.title("Alphabet Trading Volume")
plt.xticks(rotation=45)
plt.show()