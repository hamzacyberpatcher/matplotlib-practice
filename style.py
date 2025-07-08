import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

# use this to get different styles
style.use("ggplot")

data_a = np.random.random(5) * 100
data_b = np.random.random(5) * 100
data_c = np.random.random(5) * 100

# can plot multiple graphs if u want
plt.plot(data_a, label="my life")
plt.plot(data_b, label="my income")
plt.plot(data_c, label="my will to live")

# sets the legends
plt.legend(loc="lower right")

plt.show()