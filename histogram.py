import numpy as np
import matplotlib.pyplot as plt

# gives a normal distribution with a mean of 30, standard deviation of 1.75 with 1000 values
ages = np.random.normal(30, 1.75, 1000)

# 'ages' is the dataset u want
# 'bins' set the bins u want
#    u can set it the number of bins u want using bins = x, where x is the number of bins
#    or u can specify a list e.g. bins=[ages.min(), 18, 21, ages.max()]
# 'cumulative' sets the graph as cumulative histogram if set to true
plt.hist(ages, bins=20, cumulative = True)
plt.show()