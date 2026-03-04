import pandas as pd

# Load the data
df = pd.read_csv('world_alcohol.csv')

# Display dimensions/shape
print("Dimensions of the dataset (Rows, Columns):")
print(df.shape)

# Display column names
print("\nColumn names:")
print(df.columns.tolist())