import matplotlib.pyplot as plt
import numpy as np

# Sample Data
men_means = (22, 30, 35, 35, 26)
women_means = (25, 32, 30, 35, 29)
men_std = (4, 3, 4, 1, 5)
women_std = (3, 5, 2, 3, 3)
ind = np.arange(5)    

# Create the plot
plt.bar(ind, men_means, width=0.35, yerr=men_std, label='Men', color='blue')
plt.bar(ind, women_means, width=0.35, bottom=men_means, yerr=women_std, label='Women', color='red')

plt.ylabel('Scores')
plt.title('Scores by Group and Gender with Error Bars')
plt.xticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5'))
plt.legend()
plt.show()