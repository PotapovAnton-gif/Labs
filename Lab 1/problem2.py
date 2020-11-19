import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import matplotlib.pyplot as plt

f = open("/home/antpotapov2019/Frames/frames.dat", 'r')

N = f.readline()

for i in range(int(N)):

    x = np.array([coord for coord in f.readline().split()], dtype=np.float64)
    y = np.array([caord for caord in f.readline().split()], dtype=np.float64)


    ax = plt.subplot(161 + i)
    plt.grid(True)
    ax.set(xlim=(0,16 ), ylim=(-10, 10))
    plt.title('Frame {}'.format(i+1))
    plt.plot(x,y)

plt.show()
