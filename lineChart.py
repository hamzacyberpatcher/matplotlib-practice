import numpy as np
import matplotlib.pyplot as plt

# 2 lists to show on line chart
years = [2020 + x for x in range(5)]
salary = [1000, 2000, 500, 200, 10000]

print(years)

# default plot function plots a line chart
# years is in the place for x values
# salary is in the place for y values
# in "r--", 'r' represents the color red, and '--' represents that the line is going to be dashed
# lw is used to represent line width
plt.plot(years, salary, "r--", lw = 4)
plt.show()