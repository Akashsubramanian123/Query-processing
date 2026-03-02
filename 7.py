import pandas as pd

# Load the data
df = pd.read_csv('sales_data.csv')

# Create Pivot Table
pivot = df.pivot_table(index='Item', values='Sale_amt', aggfunc=['max', 'min'])

print("Maximum and Minimum Sale Value per Item:")
print(pivot)