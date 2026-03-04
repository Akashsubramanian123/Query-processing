import pandas as pd
import matplotlib.pyplot as plt

# Load the financial data
df = pd.read_csv('fdata.csv')

# Plotting
plt.plot(df['Date'], df['Close'], marker='o')

# Adding labels and title
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.title('Alphabet Inc. Stock Prices (Oct 2016)')

# Rotation for better date visibility
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig('q24_financial_plot.png')
plt.show()