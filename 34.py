import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(30)
y = np.random.rand(30)
sizes = np.random.rand(30) * 1000  # Scale for visibility

plt.scatter(x, y, s=sizes, alpha=0.5, color='orange')
plt.title('Scatter Plot with Variable Ball Sizes')
plt.show()