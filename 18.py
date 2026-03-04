import pandas as pd

# Load the data
df = pd.read_csv('school_data.csv')

# Group by school_code and class
multi_grouped = df.groupby(['school_code', 'class'])

print("Groups based on School Code and Class:")
for name, group in multi_grouped:
    print(f"\nGroup: {name}")
    print(group)