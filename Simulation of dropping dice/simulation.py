import matplotlib
import matplotlib.pyplot as plt
import random

x = [0, 100, 0]
y = [0, 0, 100]


plt.plot(x, y, ',')

curr_point = [random.randint(0,100), random.randint(0,100)]

for i in range(100000):
    j = random.randint(0,2)
    plt.plot(curr_point[0], curr_point[1], ',')
    curr_point[0] = (curr_point[0] + x[j])/2
    curr_point[1] = (curr_point[1] + y[j])/2

plt.show()