# NIM/Nama	  	: 16520002/Eraraya Morenzo Muten
# Tanggal	  	  : 18 November 2020
# Shift/Kelas	  : 3.1/a
# Deskripsi		  : Program yang menghitung jumlah mobil yang didapatkan anak Tuan 
#                 Mor dengan pembagian

# Soal 1

# Program Bagi Mobil

# KAMUS
# M, N : integer
# A, T : array of integer

# ALGORITMA
M = int(input("Masukkan M: "))                                                  # deklarasi variabel M untuk jumlah mobil, asumsi M integer positif

A = [0 for i in range(M)]                                                       # deklarasi variabel A untuk array plat mobil

for i in range(M):
  A[i] = int(input("Masukkan pelat nomor mobil ke-"+str(i+1)+": "))             # mengisi array A sesuai plat mobil dari input

N = int(input("Masukkan N: "))                                                  # deklarasi variabel N untuk jumlah anak, asumsi N>0

T = [0 for i in range(N)]                                                       # deklarasi variabel T untuk jumlah mobil yang didapat anak
for i in range(N):
  for j in range(M):
    if A[j]%(j+1) == j:
      T[i]+=1                                                                   # menambahkan jumlah mobil yang didapat anak ketika plat mobil memenuhi kriteria

sisa = M                                                                        # deklarasi variabel M untuk jumlah mobil yang didapat anak terakhir
for i in range(N-1):
  sisa = sisa - T[i]                                                            # anak terakhir mendapatkan sisa mobil
  

for i in range(N-1):                                                            # cetak jumlah mobil yang didapatkan masing-masing anak
  print("Anak ke-"+str(i+1)+" mendapatkan "+str(T[i])+" mobil")
print("Anak ke-"+str(N)+" mendapatkan "+str(sisa)+" mobil")