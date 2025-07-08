import random
import matplotlib.pyplot as plt

head_tails = [0, 0]

for _ in range(1000):
    head_tails[random.randint(0, 1)] += 1
    plt.bar(["head", "tails"], head_tails, color = ["magenta", "cyan"])

    # shows the plot, waits for 0.01s and than shows the next plot
    plt.pause(0.01)

plt.show()