import matplotlib.pyplot as plt
import numpy as np

# Group 1
w1 = [65, 68, 70, 72]
h1 = [170, 175, 172, 180]
# Group 2
w2 = [80, 85, 82, 88]
h2 = [160, 162, 165, 168]
# Group 3
w3 = [55, 58, 60, 52]
h3 = [150, 155, 152, 148]

plt.scatter(w1, h1, label='Group 1', marker='*')
plt.scatter(w2, h2, label='Group 2', marker='o')
plt.scatter(w3, h3, label='Group 3', marker='x')

plt.xlabel('Weight')
plt.ylabel('Height')
plt.title('Weight vs Height Comparison')
plt.legend()
plt.show()