# NIM/Nama	  	: 16520002/Eraraya Morenzo Muten
# Tanggal	  	  : 02 Desember 2020
# Shift/Kelas	  : 3.1/a
# Deskripsi		  : Program yang mencetak matriks segitiga pascal berukuran NxN

# Soal 3

# Program Segitiga Pascal

#KAMUS
# N : integer
# A : array of integer

#ALGORITMA
N = int(input("Masukkan N: "))                                                  # menerima input jumlah baris dan kolom matriks, asumsi N integer tidak negatif

A = [[1 for i in range(N)] for j in range(N)]                                   # membuat matriks A (NxN) berisi angka satu

for i in range(1,N):                                                            # perulangan untuk setiap elemen dalam matriks A selain baris dan kolom pertama
  for j in range(1,N):
    A[i][j] = A[i-1][j]+A[i][j-1]                                               # untuk setiap elemen yang diakses, elemen tersebut adalah jumlah dari elemen di atas dan kirinya

for i in range(N):                                                              # perulangan untuk setiap elemen dalam matriks A
  for j in range(N):
    if j+1 < N:                                                                 # untuk tiap elemen pada indeks kolom selain kolom terakhir
      print(str(A[i][j]), end=" ")                                              # cetak tiap elemen dan sambung elemen berikutnya
    elif j+1 == N:                                                              # untuk elemen pada indeks kolom terakhir
      print(str(A[i][j]))                                                       # cetak elemen tersebut dan lanjut ke line berikutnya