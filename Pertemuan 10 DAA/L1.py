import pulp

'''
Carilah nilai x dan y dari persamaan berikut
4x+ 3y = 34
5x+ y = 37

'''

model = pulp.LpProblem("ProfitMaximisingProblem", pulp.LpMaximize)
X = pulp.LpVariable('X', lowBound=0, cat="Integer")
Y = pulp.LpVariable('Y', lowBound=0, cat=" Integer")


# objective function
model += 5000 * X + 2500 * Y, "Nice"
# Constraints

model += 4 * X + 2 * Y <= 34
model += 5 * X + Y <= 37


'''gunakan fungsi penyelesaian untuk menghasilkan solusi:
'''
# solve our Problem
model.solve()
pulp.LpStatus[model.status]

'''Kemudian, cetak nilai A dan B dan nilai fungsi tujuan:
'''
# print our decision variable values
print(X.varValue)
print(Y.varValue)

# print our obj func value
print(pulp.value(model.objective))
