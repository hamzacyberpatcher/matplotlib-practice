import numpy as np
import matplotlib.pyplot as plt

# gets ur 3d projection
axs = plt.axes(projection = "3d")

x = np.random.random(100)
y = np.random.random(100)
z = np.random.random(100)

axs.scatter(x, y, z)
plt.show()