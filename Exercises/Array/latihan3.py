# Program MinArray
# Mencari nilai terkecil pada array

# KAMUS
# N : int
# T : array [0..N-1] of int
# i : int
# max : int

# ALGORITMA
N = 5 # assign N dengan ukuran T

T = [0 for i in range(N)]

for i in range(N):
    T[i] = int(input('Elemen ke-' + str(i+1) + ': '))
    
# Tetap harus dibuat untuk mengetes program
# Mencari nilai minimum
min = T[0] # init min dgn elemen pertama
# Pencarian dimulai dari elemen ke-2
for i in range(1,N):
    # jika ada elemen < min, ganti nilai min
    if (T[i] < min):
        min = T[i]
# Cetak nilai terkecil
print ("Nilai terkecil = " + str(min))
