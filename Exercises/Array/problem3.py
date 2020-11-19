X = int(input("Masukkan X: "))
titik = [0 for i in range(X)]
for i in range(X):
    titik[i] = int(input("Kondisi titik ke-" + str(i) + ": "))

C = int(input("Masukkan titik lokasi bom [C]: "))
L = int(input("Masukkan daya ledak bom [L]: "))

aman = 0
for i in range(0, C-L):
    if titik[i] == 1:
        aman += 1

for i in range(C+L+1, X):
    if titik[i] == 1:
        aman += 1

if aman == 0:
    print("Tidak ada titik yang bisa kamu tempati")
else:
    print("Ada", aman, "titik yang bisa kamu tempati.")