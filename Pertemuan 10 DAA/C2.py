"""
Menggunakan Scipy
Persamaan max z = 5x1 + 7x2 dimana
1x1 + 0x2 <= 16,
2x1 + 3x2 <= 19,
1x1 + 1x2 <= 8,
x1, x2 >= 0

"""
import numpy as np
from scipy.optimize import linprog

A = np.array([[1, 0], [2, 3], [1, 1], [-1, 0], [0, -1]])
b = np.array([16, 19, 8, 0, 0])
c = np.array([-5, -7])
res = linprog(c, A_ub=A, b_ub=b)

print('Optimal value:', round(res.fun*-1, ndigits=2),
      '\nx values:', res.x,
      '\nNumber of iterations performed:', res.nit,
      '\nStatus:', res.message)


