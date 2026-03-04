import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('fdata.csv')

# Plotting two lines
plt.plot(df['Date'], df['Open'], color='blue', linewidth=3, label='Open Price')
plt.plot(df['Date'], df['Close'], color='red', linewidth=5, label='Close Price')

# Adding labels, title, and legend
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Open vs Close Prices')
plt.legend()

plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('q25_multiple_lines.png')
plt.show()