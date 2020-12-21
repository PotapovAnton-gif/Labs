from sympy import *
import matplotlib
import matplotlib.pyplot as plt
import scipy 

t = symbols('t')
y = Function('y')

E1 = dsolve(Eq (y (t) .diff (t) - 2 * y (t),0), y(t))
print(solve(E1, y(0) == sqrt(2)))

