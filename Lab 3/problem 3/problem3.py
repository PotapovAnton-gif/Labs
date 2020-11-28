import numpy as np
import pandas as pd
import requests
from functools import reduce

data1 = pd.read_html("/home/antpotapov2019/labs_for_py/Lab 3/problem 3/results_ejudge.html")
data2 = pd.read_excel("/home/antpotapov2019/labs_for_py/Lab 3/problem 3/students_info.xlsx")

data2.rename(columns= {'login':'User'}, inplace=True)


data1.
print(data1)




