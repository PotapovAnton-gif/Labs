import matplotlib

matplotlib.use('TkAgg')
import numpy as np
import matplotlib.pyplot as plt

f = open('/home/antpotapov2019/students.csv')
x = []

x.append([i.split(';') for i in f.read().split()])
x = x[0]
prep = x.copy()
grups = x.copy()

for i in range(len(x)):
    del prep[i][0]
    

print(grups)

