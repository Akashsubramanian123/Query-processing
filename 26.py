import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('fdata.csv')

# Create subplots (1 row, 2 columns)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

# First plot: Open Price
ax1.plot(df['Date'], df['Open'], color='blue')
ax1.set_title('Open Prices')
ax1.set_xlabel('Date')
ax1.tick_params(axis='x', rotation=45)

# Second plot: Close Price
ax2.plot(df['Date'], df['Close'], color='green')
ax2.set_title('Close Prices')
ax2.set_xlabel('Date')
ax2.tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.savefig('q26_subplots.png')
plt.show()