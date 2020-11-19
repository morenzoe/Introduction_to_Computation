# Program TambahVektor
# Menambah elemen tiap vektor V dan U dan disimpan ke vektor W

# KAMUS
# V, U, W: array [0..5] of int
# i: int

# ALGORITMA
V = [0 for i in range(5)]
U = [0 for i in range(5)]
W = [0 for i in range(5)]

for i in range(5):
    V[i] = int(input())

for i in range(5):
    U[i] = int(input())

for i in range(5):
    W[i] = V[i] + U[i]

print(W)
