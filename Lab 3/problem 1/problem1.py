import numpy as np

import pandas as pd

data = pd.read_csv(r"C:\Users\antho\Labs\Lab 3\problem 1\transactions.csv")

data = data[lambda x: x['STATUS'] == 'OK']

data.sort_values('SUM', inplace = True, ignore_index = True)

print([data['SUM'][i] for i in range(int(data.shape[0]) -3,int(data.shape[0]),1)])
print(data['SUM'].sum())