import pandas as pd

# Load the data
df = pd.read_csv('orders_missing_data.csv')

# Detect missing values (True for NaN, False for present)
print("Missing values detection (True/False):")
print(df.isna())