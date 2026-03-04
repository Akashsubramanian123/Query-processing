import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(50)
y = np.random.randn(50)

plt.scatter(x, y, facecolors='none', edgecolors='green', s=80)
plt.title('Scatter Plot with Empty Circles')
plt.show()