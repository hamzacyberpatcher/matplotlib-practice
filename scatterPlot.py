import numpy as np

# common convention to include matplotlib like this
import matplotlib.pyplot as plt

# gives 2 lists with 1000 memebers with vals between 0 and 1. multiply them will 100.
x_data = np.random.random(1000) * 100
y_data = np.random.random(1000) * 100

# plots the data as a scatter plot
# x_data is the x values
# y_data is the y values
# c is the color of the points
# marker is the shape of the points, by default it is a dot (duh)
# s is the size of the point
# alpha is the transparency of the point (useful if u have a lot of points)
plt.scatter(x_data, y_data, c = "RED", marker = "*", s=150, alpha = 0.3)

# shows the scatter plot (most prolly it is not needed if u r using jupyter notebook, but i've frankly had enough of it and i just cannot bear anymore to see more of it, fuck condas, although jupyter notebook was a W tool)
plt.show()