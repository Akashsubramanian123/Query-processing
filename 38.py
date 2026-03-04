import pandas as pd

# Load from your CSV
df = pd.read_csv('exam_data.csv')

# Set the labels column as the index
df.set_index('labels', inplace=True)

print("Exam Data with Index Labels:")
print(df)