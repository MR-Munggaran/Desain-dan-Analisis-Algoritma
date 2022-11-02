import numpy as np
from scipy.optimize import linprog


A = np.array([[3, 4], [1, 1], [-1, 0], [0, -1]])
b = np.array([55, 16, 0, 0])
c = np.array([-1, -1])
res = linprog(c, A_ub=A, b_ub=b)

print('Optimal value:', round(res.fun*-1, ndigits=2),
      '\nx values:', res.x,
      '\nNumber of iterations performed:', res.nit,
      '\nStatus:', res.message)
