import numpy as np
import pandas as pd
import ma

data = pd.read_csv(r"C:\Users\antho\Labs\Lab 3\problem 2\flights.csv")

Nimble = data[lambda x: x['CARGO'] == 'Nimble']
Medium = data[lambda x: x['CARGO'] == 'Medium']
Jumbo = data[lambda x: x['CARGO'] == 'Jumbo']

