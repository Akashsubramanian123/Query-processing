import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('languages.csv')

# Create bar chart
plt.bar(df['Language'], df['Popularity'])

# Add labels and title
plt.xlabel('Programming Languages')
plt.ylabel('Popularity (%)')
plt.title('Popularity of Programming Languages')

plt.savefig('q27_bar_chart.png')
plt.show()