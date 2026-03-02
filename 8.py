import pandas as pd

# Load the data
df = pd.read_csv('sales_data.csv')

# Create Pivot Table
pivot = df.pivot_table(index='Item', values='Units', aggfunc='sum')

print("Total Units Sold per Item:")
print(pivot)