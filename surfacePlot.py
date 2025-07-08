import numpy as np
import matplotlib.pyplot as plt

ax = plt.axes(projection="3d")

x, y = np.arange(-5, 5, 0.1), np.arange(-5, 5, 0.1)

# creates a meshgrid out of x and y
X, Y = np.meshgrid(x, y)

Z = np.sin(X) + np.cos(Y)

# cmap basically sets the color styles for the elevations and the bumps
ax.plot_surface(X, Y, Z, cmap="Spectral")
ax.set_title("z = sin(x) + sin(y)")
ax.view_init(azim = 45, elev = 90)

plt.show()