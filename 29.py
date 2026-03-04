import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('languages.csv')

# Define colors
colors = ['red', 'blue', 'green', 'yellow', 'cyan', 'magenta']

# Create bar chart with colors
plt.bar(df['Language'], df['Popularity'], color=colors)

plt.xlabel('Programming Languages')
plt.ylabel('Popularity (%)')
plt.title('Colored Bar Chart of Language Popularity')

plt.savefig('q29_colored_bar.png')
plt.show()