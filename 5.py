import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('alphabet_stock_data.csv')
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Filter for a specific week
df_filtered = df.loc['2020-04-01':'2020-04-07']

# Plot trading volume
df_filtered['Volume'].plot(kind='bar', title='Alphabet Inc. Trading Volume')
plt.ylabel('Volume')
plt.savefig('alphabet_bar_plot.png')
plt.show()