import pandas as pd

# Load the data
df = pd.read_csv('jobs.csv')

# Sort by job title in descending order
result = df.sort_values('JOB_TITLE', ascending=False)

print("Job details sorted by title (Descending):")
print(result)