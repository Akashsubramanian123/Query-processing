import pandas as pd

# Load the data
df = pd.read_csv('school_data.csv')

# Group by school_code and calculate stats for age
age_stats = df.groupby('school_code')['age'].agg(['mean', 'min', 'max'])

print("Age Statistics per School:")
print(age_stats)