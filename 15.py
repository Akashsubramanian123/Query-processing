import pandas as pd

# Load the data
df = pd.read_csv('nan_data.csv')

# Filter: keep rows with at least 2 NaN values
# thresh=n keeps rows with at least n non-NaN values. 
# Since there are 5 columns, keeping rows with >=2 NaNs means keeping rows with <=3 non-NaNs.
result = df[df.isnull().sum(axis=1) >= 2]

print("Rows with at least 2 NaN values:")
print(result)