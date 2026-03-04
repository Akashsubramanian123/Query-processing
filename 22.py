import matplotlib.pyplot as plt

# Data for plotting
x = [1, 2, 3]
y = [2, 4, 1]

# Plotting the line
plt.plot(x, y)

# Adding labels and title
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Simple Line Graph')

# Save and show
plt.savefig('q22_line_plot.png')
plt.show()