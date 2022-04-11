# Aryan Sharan Reddy
## BT21BTECH11002
# Q) 8(C)

import matplotlib.pyplot as plt
import numpy as np


figure, axes = plt.subplots()
Drawing_uncolored_circle = plt.Circle((0, 0), 3.5, fill=False) # Drawing a circle.

axes.set_aspect(1)
axes.add_artist(Drawing_uncolored_circle)

#plt.plot([-3.5, 0], [3.5, 0], 'b')# Diameter of our circle BC

#Plotting the points
plt.plot([0], [0], 'o')
plt.plot([0], [3.5], 'o') 
plt.plot([3.5], [0], 'o')
plt.plot([-3.5], [0], 'o')
plt.plot([2.48], [2.48], 'o')


#Plotting the line segments
#plt.plot([-3.5, 0], [3.5, 0], 'b')# Diameter of our circle BC
plt.plot([-3.5, 3.5, 2.475, 0, -3.5, 2.475], [0, 0, 2.475, 3.5, 0, 2.475], 'b') # Line segment BO



# Labelling the points, put a small offset so that the labels are not overlapping.
plt.annotate('O', xy=(0, 0), textcoords='data')
plt.annotate('A', xy=(0, 3.5+0.3), textcoords='data')
plt.annotate('B', xy=(-3.5-0.3, 0), textcoords='data')
plt.annotate('D', xy=(2.48+0.3, 2.48+0.3), textcoords='data')
plt.annotate('C', xy=(3.5+0.3, 0), textcoords='data')


plt.xticks(np.arange(-4, 4))
plt.yticks(np.arange(-4, 4))

plt.show()
