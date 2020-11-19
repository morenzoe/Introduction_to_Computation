# Program KaliArray
# Mengalikan array dengan suatu bilangan

# KAMUS
# T : array [0..19] of int
# X : int

# ALGORITMA
T = [0 for i in range(20)]
for i in range(20):
    T[i] = int(input("T"+str(i+1)+": "))
    
X = int(input("X: "))

for i in range(20):
    T[i] *= X
    print(T[i], end=" ")
