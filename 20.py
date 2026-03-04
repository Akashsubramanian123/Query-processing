import pandas as pd

# Load the data
df = pd.read_csv('school_data.csv')

# Find the index of substring 'Franco' in the 'name' column
# This returns the position within the string, or -1 if not found
df['substring_index'] = df['name'].str.find('Franco')

print("Rows where 'Franco' index was found:")
print(df[['name', 'substring_index']])