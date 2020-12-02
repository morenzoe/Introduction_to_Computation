# NIM/Nama	  	: 16520002/Eraraya Morenzo Muten
# Tanggal	  	  : 02 Desember 2020
# Shift/Kelas	  : 3.1/a
# Deskripsi		  : Program yang memeriksa jumlah bilangan positif matriks

# Soal 2

# Program Pencari Positif

#KAMUS
# N, M : integer
# A : array of integer

#ALGORITMA
N = int(input("Masukkan N: "))                                                  # menerima input jumlah baris matriks, asumsi N integer tidak negatif
M = int(input("Masukkan M: "))                                                  # menerima input jumlah kolom matriks, asumsi M integer tidak negatif

A = [[0 for i in range(M)] for j in range(N)]                                   # membuat matriks A (MxN) berisi angka nol

pos = 0                                                                         # variabel untuk menyimpan jumlah bilangan positif di dalam matriks A

for i in range(N):                                                              # perulangan untuk setiap elemen dalam matriks A
  for j in range(M):
    A[i][j] = int(input("Masukkan nilai A["+str(i+1)+"]["+str(j+1)+"]: "))      # menerima input elemen matriks, asumsi input integer
    if A[i][j] > 0:
      pos+=1                                                                    # jika nilai input positif, tambahkan 1 pada variabel pos

print("Ada "+str(pos)+" bilangan positif di matriks.")                          # cetak jumlah bilangan positif dalam matriks


for i in range(N):                                                              # perulangan untuk setiap elemen dalam matriks A
  for j in range(M):
    if j+1 < M:                                                                 # untuk tiap elemen pada indeks kolom selain kolom terakhir
      print(str(A[i][j]), end=" ")                                              # cetak tiap elemen dan sambung elemen berikutnya
    elif j+1 == M:                                                              # untuk elemen pada indeks kolom terakhir
      print(str(A[i][j]))                                                       # cetak elemen tersebut dan lanjut ke line berikutnya