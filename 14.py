import pandas as pd

# Load the data
df = pd.read_csv('orders_missing_data.csv')

# Replace missing values with 0
df_filled = df.fillna(0)

print("Original Data with NaNs:")
print(df.head())
print("\nData after replacing NaNs with 0:")
print(df_filled.head())