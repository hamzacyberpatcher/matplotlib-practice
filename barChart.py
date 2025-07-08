import numpy as np
import matplotlib.pyplot as plt

cars = ["miata", "supra", "mustang", "gallardo", "RX-8"]
sales = [2000, 1500, 1800, 250, 2100]

# cars is in the place for horizontal markers
# sales goes in the place for the vertical values
plt.bar(cars, sales)
plt.show()