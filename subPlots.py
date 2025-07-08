import numpy as np
import matplotlib.pyplot as plt

x = np.arange(100)

# gives 2 rows and 2 cols
figs, axs = plt.subplots(2, 2)

# first row, first col graph
axs[0, 0].plot(x, np.sin(x))
axs[0, 0].set_title("Sine Wave")

# first row, second col graph
axs[0, 1].plot(x, np.cos(x))
axs[0, 1].set_title("Cosine Wave")

# second row, first col graph
axs[1, 0].plot(x, np.random.random(100))
axs[1, 0].set_title("Random Wave")

# second row, second col graph
axs[1, 1].plot(x, np.log(x))
axs[1, 1].set_title("Log Wave")

figs.suptitle("Plots Muhahahahaha")

plt.tight_layout()
plt.show()