# Program SearchArray
# Mencari indeks di mana X ditemukan terakhir kali di T

# KAMUS
# N : int; ukuran T
# T : array [0..N-1] of int
# i, X : int
# found : bool; menentukan X sdh ditemukan/belum

# ALGORITMA
N = 5 # assign N dengan ukuran T

T = [0 for i in range(N)]

for i in range(N):
    T[i] = int(input())

# Membaca nilai yang dicari, yaitu X
X = int(input("Masukkan nilai yang dicari: "))
# Pencarian dimulai dari elemen ke-N-1
i = N-1
found = False # found = False; X belum ditemukan
while (i >= 0 and found == False):
    if (T[i] == X):
        found = True # found = True; X sudah ditemukan
    else:
        i = i - 1 # hanya decrement jika X belum ditemukan
# i = 0 atau found = True
# Cetak Hasil
if (found == True): # X ditemukan di T
    print (str(X) + " ditemukan di indeks ke-" + str(i))
else: # found = False; X tidak ditemukan di T
    print (str(X) + " tidak ditemukan")
