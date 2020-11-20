import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import matplotlib.pyplot as plt
from filtr import filt


f = open('/home/antpotapov2019/signals/signal03.dat', 'r')

y =[float(i) for i in f.read().split('\n')]
x =[i for i in range(100)] 

new_y = filt(y, 100)
plt.subplot(121)
plt.plot(x, y)
plt.subplot(122)
plt.plot(x, new_y)
plt.show()


