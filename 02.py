import pandas as pd

# Load the data
df = pd.read_csv('job_history.csv')

# Group by Employee ID and count occurrences
job_counts = df.groupby('EMPLOYEE_ID').size()

# Filter for those with 2 or more jobs
result = job_counts[job_counts >= 2].index

print("Employee IDs with two or more jobs:")
print(result.tolist())