import numpy as np
import pandas as pd
import requests

data1 = pd.read_html("/home/antpotapov2019/labs_for_py/Lab 3/problem 3/results_ejudge.html")
data2 = pd.read_excel("/home/antpotapov2019/labs_for_py/Lab 3/problem 3/students_info.xlsx")

take_smaller = lambda s1, s2: s1 if s1.sum() < s2.sum() else s2

data2.rename(columns= {'login':'User'}, inplace=True)

df.join(other.set_index('key'), on='key')

print(data2)




