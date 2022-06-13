# Import libraries
import matplotlib.pyplot as plt
import numpy as np

# Creating vectors X and Y
x = np.linspace(0, 10, 100)
y = (1/((5-x) ** 2 + (2*x) ** 2)) ** 1/2

fig = plt.figure(figsize = (10, 5))
# Create the plot
plt.plot(x, y)

plt.plot([np.sqrt(3)], [0], 'o')

plt.annotate('A', xy=(np.sqrt(3)+0.3 , 0), textcoords='data')

# Show the plot
plt.show()
