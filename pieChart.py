import numpy as np
import matplotlib.pyplot as plt

# labels for the dataset
labels = ["miata", "dala", "RX-8", "Murci", "GT8"]
# their values
sales = [1000, 2000, 200, 1500, 800]
# sets how much the data should be pulled out from the center of the chart visually
explodes = [0.2, 0, 0, 0, 0]

# 'sales' goes in the place for the neumrical data
# 'labels' are the labels for those repective sales
# 'explodes' sets the explodes values for the data set
# 'autopct' displays the percentage of each piece in the pie
# 'pctdistance' sets the distance of the percentage label from the center of the pie
# 'startangle' sets the startangle of the pie chart
plt.pie(sales, labels=labels, explode=explodes, autopct="%.1f%%", pctdistance=0.4, startangle=45)
plt.show()