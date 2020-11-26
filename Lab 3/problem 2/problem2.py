import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\antho\Labs\Lab 3\problem 2\flights.csv")

CARGO = [0]*3

CARGO[0] = data[lambda x: x['CARGO'] == 'Nimble']
CARGO[1] = data[lambda x: x['CARGO'] == 'Medium']
CARGO[2] = data[lambda x: x['CARGO'] == 'Jumbo']

listw = ('Nimble', 'Medium', 'Jumbo')
shapes = [CARGO[i].shape[0] for i in range(3)]
plt.subplot(131)
plt.bar(listw,shapes)
plt.title('Number of flights')

weight = [CARGO[i]['WEIGHT'].sum() for i in range(3)]
plt.subplot(132)
plt.bar(listw,weight)
plt.title('Total weight')

price = [CARGO[i]['PRICE'].sum() for i in range(3)]
plt.subplot(133)
plt.bar(listw, price)
plt.title('Total price')

plt.show()


