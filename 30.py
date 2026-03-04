import matplotlib.pyplot as plt
import numpy as np

# Sample Data
groups = ('G1', 'G2', 'G3', 'G4', 'G5')
men_means = (22, 30, 35, 35, 26)
women_means = (25, 32, 30, 35, 29)

# Creating the plot
index = np.arange(len(groups))
bar_width = 0.35

# Plotting bars for Men and Women side-by-side
plt.bar(index, men_means, bar_width, label='Men', color='blue')
plt.bar(index + bar_width, women_means, bar_width, label='Women', color='red')

# Adding labels and title
plt.xlabel('Group')
plt.ylabel('Scores')
plt.title('Scores by group and gender')
plt.xticks(index + bar_width / 2, groups)
plt.legend()

plt.savefig('q30_grouped_bar.png')
plt.show()