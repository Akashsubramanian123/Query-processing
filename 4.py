import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('alphabet_stock_data.csv')
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Define date range
start_date = '2020-04-01'
end_date = '2020-04-30'

# Filter and plot
df_filtered = df.loc[start_date:end_date]
df_filtered['Close'].plot(kind='line', title='Alphabet Inc. Stock Prices')
plt.ylabel('Price')
plt.savefig('alphabet_line_plot.png')
plt.show()