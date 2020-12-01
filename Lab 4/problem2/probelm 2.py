import numpy as np
from scipy import linalg
import matplotlib
import matplotlib.pyplot as plt

f = open('/home/antpotapov2019/labs_for_py/Lab 4/problem2/small.txt')
N = int(f.readline())
A = []
for i in range(N):
    string = [float(k) for k in f.readline().split()]
    A.append(string)
A = np.array(A)
B = np.array([float(k) for k in f.readline().split()])

x = linalg.solve(A, B)
l = [i for i in range(3)]

plt.bar(l, x)
plt.grid()
plt.show()


