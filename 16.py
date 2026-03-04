import pandas as pd

# Load the data
df = pd.read_csv('school_data.csv')

# Group by school code
grouped = df.groupby('school_code')

print("Type of GroupBy object:")
print(type(grouped))

# Display groups
for name, group in grouped:
    print(f"\nGroup: {name}")
    print(group)