import numpy as np
import matplotlib.pyplot as plt

years = [2010, 2011, 2012, 2013, 2014]
sales = [100, 500, 200, 600, 550]
sales_ticks = list(range(90, 591, 50))

plt.plot(years, sales)
plt.title("Yearly sales in USD", fontsize=20, fontname="calibri") # sets the title for the plot
plt.xlabel("Years")        # sets the xlabel
plt.ylabel("Sales in USD") # sets the y label
plt.xticks(years)          # sets the ticks for the x axis
plt.yticks(sales_ticks, [f"${x}" for x in sales_ticks]) # sets the ticks for y axis
plt.show()