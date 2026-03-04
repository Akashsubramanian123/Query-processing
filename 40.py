import pandas as pd

df = pd.read_csv('exam_data.csv')

# Selecting multiple columns
selected_columns = df[['name', 'score']]

print("Selected Columns (Name and Score):")
print(selected_columns)