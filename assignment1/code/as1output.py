import matplotlib.pyplot as plt
import numpy as np

###
#### Aryan Sharan Reddy
#### BT21BTECH11002
###

#### Q8 c)

x=90
Angle_BAC=x
#angle in a semicircle is 90
Angle_ABC=90-(x)/2
#Angle_BAC+Angle_ABC+Angle_ACB=180
#Angle_ABC=Angle_ACB
#In a cyclic quadrilateral, opposite angles are always supplementary
Angle_ADC=180-(Angle_ABC)
y=Angle_ADC
print("y=",y,chr(176),sep='')

figure, axes = plt.subplots()

axes.set_aspect(1)

a = np.linspace(0,2*np.pi,100000)

# r = 2, y' = x' = 0
y1 = 3.5*np.sin(a) # y = r sin(a) + y'
x1 = 3.5*np.cos(a) # x = r cos(a) + x'

plt.plot(x1, y1)

# The inputs
r = 3.5
theta = (np.pi)/2

# The Points
#O = [0,0]
#Q = [4,-r]
A = [0, r]
B = [-r, 0]
C = [r, 0]
D = [-3.5+2*r*np.cos((np.pi-theta)/4)*np.cos((np.pi-theta)/4), 2*r*np.cos((np.pi-theta)/4)*np.sin((np.pi-theta)/4)]

def plot_point(P):
    plt.plot(P[0], P[1], marker = 'o')

def plot_line_segment(P1, P2):
    plt.plot([P1[0], P2[0]], [P1[1], P2[1]], 'b')

def mark_point(P, lab):
    plt.annotate(lab, xy=(P[0] - 0.3, P[1] + 0.3), textcoords='data')

#Plotting the points
plot_point(A)
plot_point(B)
plot_point(C)
plot_point(D)
#plot_point(P)
#plot_point(Q)
plt.plot([0], [0], 'o') # Center of the circle

#Plotting the line segments
#plot_line_segment(P, Q) # Tangent to thr circle (PQ)
#plot_line_segment(O, B) # Line segment OB
plot_line_segment(D, A) # Line segment DA
plot_line_segment(B, A) # Line segment BA
plot_line_segment(D, B) # Line segment DB
plot_line_segment(D, C) # Line segment DC
plot_line_segment(B, C) # Line segment BC

# Labelling the points, put a small offset so that the labels are not overlapping.
mark_point(A, 'A')
mark_point(B, 'B')
mark_point(C, 'C')
mark_point(D, 'D')
#mark_point(P, 'P')
#mark_point(Q, 'Q')

plt.xticks(np.arange(-4, 4))
plt.yticks(np.arange(-4, 4))

plt.show()
