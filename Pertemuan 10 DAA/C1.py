import pulp

'''
Pertama, impor paket Python bernama pulp, 
yang digunakan untuk mengimplementasikan pemrograman linier:

'''
model = pulp.LpProblem("ProfitMaximisingProblem", pulp.LpMaximize)
'''
Kemudian, panggil fungsi LpProblem dalam paket ini untuk membuat instance kelas masalah. 
beri nama instance Profit maximising problem:
Kemudian, tentukan dua variabel linier, A dan B. 

Variabel A mewakili jumlah robot tingkat lanjut yang diproduksi 
dan variabel B mewakili jumlah robot dasar yang diproduksi:

'''
A = pulp.LpVariable('A', lowBound=0, cat="Integer")
B = pulp.LpVariable('B', lowBound=0, cat=" Integer")

'''mendefinisikan fungsi tujuan dan kendala sebagai berikut:'''

# objective function
model += 5000 * A + 2500 * B, "Profit"
# Constraints

model += 3 * A + 2 * B <= 20
model += 4 * A + 3 * B <= 30
model += 4 * A + 3 * B <= 44

'''gunakan fungsi penyelesaian untuk menghasilkan solusi:
'''
# solve our Problem
model.solve()
pulp.LpStatus[model.status]

'''Kemudian, cetak nilai A dan B dan nilai fungsi tujuan:
'''
# print our decision variable values
print(A.varValue)
print(B.varValue)

# print our obj func value
print(pulp.value(model.objective))

