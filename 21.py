import pandas as pd

# Load the data
df = pd.read_csv('case_data.csv')

# Swap the cases of the 'job_role' column
df['job_role'] = df['job_role'].str.swapcase()

print("Data after swapping cases in 'job_role':")
print(df)