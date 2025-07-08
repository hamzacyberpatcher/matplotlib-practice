import numpy as np
import matplotlib.pyplot as plt

cars = ["miata", "supra", "mustang", "gallardo", "RX-8"]
sales = [2000, 1500, 1800, 250, 2100]

# cars is in the place for horizontal markers
# sales goes in the place for the vertical values
# 'color' will tell the color of the bar
# 'align' will tell where to start the bar graph on the horizontal scale
# 'width' sets the width of the bar
# 'edgecolor' sets the color of the edge of the bar
# 'lw' will set the width of the edge of the bar
plt.bar(cars, sales, color = "magenta", align = "edge", width = 0.5, edgecolor = "blue", lw=4)
plt.show()