import matplotlib.pyplot as plt

# Reading data from text.txt
with open('text.txt', 'r') as f:
    lines = f.readlines()
    x = [float(line.split()[0]) for line in lines]
    y = [float(line.split()[1]) for line in lines]

# Plotting the data
plt.plot(x, y)

# Adding labels and title
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Line Graph from Text File')

# Save and show
plt.savefig('q23_text_plot.png')
plt.show()