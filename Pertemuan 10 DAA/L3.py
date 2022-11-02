import pulp

'''
Budi membeli tiga pensil dan empat buku di toko Rana dengan harga Rp 11000,-. 
Jika Budi membeli lagi sebuah pensil dan tujuh buku ditoko yang sama dengan
harga Rp 15000,-. Berapakah harga dua buah pensil dan enam buah buku jika Budi 
membeli kembali di toko Rana!


'''

model = pulp.LpProblem("ProfitMaximisingProblem", pulp.LpMaximize)
X = pulp.LpVariable('X', lowBound=0, cat="Integer")
Y = pulp.LpVariable('Y', lowBound=0, cat=" Integer")


# objective function
model += 2 * X + 2 * Y, "KEL"

# Constraints

model += 2 * X + 2 * Y <= 44
model += 2 * X + 2 * (X - 6) <= 4


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
