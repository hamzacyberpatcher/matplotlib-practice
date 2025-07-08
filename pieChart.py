import numpy as np
import matplotlib.pyplot as plt

# labels for the dataset
labels = ["miata", "dala", "RX-8", "Murci", "GT8"]
# their values
sales = [1000, 2000, 200, 1500, 800]

# 'sales' goes in the place for the neumrical data
# 'labels' are the labels for those repective sales
plt.pie(sales, labels=labels)
plt.show()