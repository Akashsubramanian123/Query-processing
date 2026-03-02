import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('alphabet_stock_data.csv')
df['Date'] = pd.to_datetime(df['Date'])

# Filter dates
df_filtered = df[(df['Date'] >= '2020-04-01') & (df['Date'] <= '2020-05-31')]

# Scatter plot
plt.scatter(df_filtered['Volume'], df_filtered['Close'], alpha=0.5)
plt.title('Trading Volume vs Stock Prices')
plt.xlabel('Volume')
plt.ylabel('Price')
plt.savefig('alphabet_scatter_plot.png')
plt.show()