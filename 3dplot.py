import numpy as np
import matplotlib.pyplot as plt

# gets ur 3d projection
axs = plt.axes(projection = "3d")

x = np.arange(0, 50, 0.1)
y = np.arange(0, 50, 0.1)
z = np.cos(x + y)

axs.plot(x, y, z)
plt.show()