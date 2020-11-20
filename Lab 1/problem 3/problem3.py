import matplotlib

matplotlib.use('TkAgg')
import numpy as np
import matplotlib.pyplot as plt

colors = ['blue', 'green', 'gray', 'black', 'red', 'orange', 'yellow', 'purple']
f = open('/home/antpotapov2019/students.csv')
x = []
x.append([i.split(';') for i in f.read().split()])
x = x[0]


prep = np.arange(56).reshape(7,8)

for i in range(7):
    for j in range(8):
        prep[i][j] = 0


for i in range(len(x)):
    for j in range(7):
        for k in range(3, 11):
            if int(x[i][0][-1]) == j+1 and int(x[i][2]) == k:
                prep[j][k-3] += 1 


groups = np.arange(48).reshape(6,8)

for i in range(6):
    for j in range(8):    
        groups[i][j] = 0

for i in range(len(x)):
    for j in range(6):
        for k in range(3, 11):
            if int(x[i][1][-1]) == j+1 and int(x[i][2]) == k:
                groups[j][k-3] += 1

plt.subplot(121)
for i in range(7):
    y = 0
    for j in range(8):
        plt.bar(i, prep[i][j], 0.8 ,y,color = colors[j])
        y += prep[i][j]

ind = np.arange(7)
plt.xticks(ind, ('P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7'))

plt.subplot(122)        
for i in range(6):
    y = 0
    for j in range(8):
        plt.bar(i, groups[i][j], 0.8 ,y,color = colors[j])
        y += groups[i][j]
ind = np.arange(6)
plt.xticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5', 'G6'))
plt.show()

