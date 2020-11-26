import numpy as np
import pandas as pd

data1 = pd.read_csv(r"C:\Users\antho\Labs\Lab 3\problem 3\students_info.csv")
data2 = pd.read_html(r"C:\Users\antho\Labs\Lab 3\problem 3\results_ejudge.html")

print(data2)


