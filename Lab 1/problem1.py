import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import matplotlib.pyplot as plt


f = open("/home/antpotapov2019/dead_moroz/005.dat", 'r')

N = f.readline()

for i in range(int(N)):
    x = [j for j in f.readline().split()]
    plt.plot(float(x[0]),float(x[1]), 'bo')

plt.show()
