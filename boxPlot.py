import numpy as np
import matplotlib.pyplot as plt

# 25 values from 0 to 10
first = np.linspace(0, 10, 25)
# 25 values from 10 to 50
second = np.linspace(10, 50, 25)
# 25 values from 50 to 100
third = np.linspace(50, 100, 35)
# 100 values from 100 to 125
fourth = np.linspace(100, 125, 10)

# concatonates all the previous lists
data = np.concatenate((first, second, third, fourth))

plt.boxplot(data)
plt.show()