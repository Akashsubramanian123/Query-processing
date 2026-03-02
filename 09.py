import pandas as pd

# Load the data
df = pd.read_csv('sales_data.csv')

# Create Pivot Table
pivot = df.pivot_table(index=['Region', 'Manager', 'SalesMan'], 
                       values='Sale_amt', 
                       aggfunc='sum')

print("Total Sale Amount (Region, Manager, Salesman):")
print(pivot)