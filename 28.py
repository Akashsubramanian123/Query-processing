import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('languages.csv')

# Create horizontal bar chart
plt.barh(df['Language'], df['Popularity'], color='skyblue')

# Add labels and title
plt.xlabel('Popularity (%)')
plt.ylabel('Programming Languages')
plt.title('Horizontal Bar Chart of Language Popularity')

plt.savefig('q28_horizontal_bar.png')
plt.show()