import pandas as pd

# Load the data
df = pd.read_csv('departments.csv')

# Select distinct department IDs
distinct_dept_ids = df['DEPARTMENT_ID'].unique()

print("Distinct Department IDs:")
print(distinct_dept_ids)