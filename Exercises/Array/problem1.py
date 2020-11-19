X = int(input("Masukkan X: "))
N = int(input("Masukkan N: "))

frek = [0 for i in range(X)]

for i in range(N):
    y = int(input()) - 1
    frek[y] += 1

maks = frek[0]
idx = 0
for i in range(1, X):
    if frek[i] > maks:
        maks = frek[i]
        idx = i

print("Pemenang pemilu adalah calon dengan nomor urut", end=" ")
print(idx+1, end="")
for i in range(idx+1, X):
    if frek[i] == maks:
        print(","+str(i+1), end="")
print()