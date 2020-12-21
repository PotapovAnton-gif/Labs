import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import random

x = []
y = []

for i in range(3):
    x.append(random.randint(0, 10))
    y.append(random.randint(0, 10))

plt.scatter(x, y, s=1)

curr_point = [random.randint(0,10), random.randint(0,10)]

for i in range(2000):
    j = random.randint(0,2)
    plt.scatter(curr_point[0], curr_point[1], s=1)
    curr_point[0] = (curr_point[0] + x[j])/2
    curr_point[1] = (curr_point[1] + y[j])/2

plt.show()