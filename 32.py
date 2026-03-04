import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(50)
y = np.random.randn(50)

plt.scatter(x, y, color='purple')
plt.title('Random Distribution Scatter Plot')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()