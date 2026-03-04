import pandas as pd
import matplotlib.pyplot as plt

# Load data from your file
df = pd.read_csv('marks_data.csv')

plt.scatter(df['marks_range'], df['math_marks'], label='Math Marks', color='red')
plt.scatter(df['marks_range'], df['science_marks'], label='Science Marks', color='blue')

plt.title('Mathematics vs Science Marks')
plt.xlabel('Marks Range')
plt.ylabel('Marks Scored')
plt.legend()
plt.show()