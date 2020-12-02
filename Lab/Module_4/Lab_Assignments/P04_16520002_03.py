# NIM/Nama	  	: 16520002/Eraraya Morenzo Muten
# Tanggal	  	  : 02 Desember 2020
# Shift/Kelas	  : 3.1/A
# Deskripsi		  : Program yang mencetak matriks segitiga pascal berukuran NxN

# Soal 3

# Program Segitiga Pascal

#KAMUS
# N, M : integer
# A : array of integer

# KAMUS LOKAL
# a, b, N, M : integer
# bol : boolean
def diagonal(a, b, N, M):                                                       # fungsi untuk cek apakah kotak terlewati diagonal
# ALGORITMA
  bol = True                                                                    # inisialisasi hasil
  p1 = M*a - N*b                                                                # untuk indeks matriks python, fungsi diagonal menjadi M*a-N*b=0
  p2 = M*(a) - N*(b+1)
  p3 = M*(a+1) - N*(b+1)
  p4 = M*(a+1) - N*(b)
  if p1>0 and p2>0 and p3>0 and p4>0:                                           # jika setiap kotak berada di atas garis, kotak tidak dilewati diagonal
    bol = False
  elif p1<0 and p2<0 and p3<0 and p4<0:                                         # jika setiap kotak berada di bawah garis, kotak tidak dilewati diagonal
    bol = False
  return bol

#ALGORITMA
N = int(input("Masukkan N: "))                                                  # menerima input jumlah baris dan kolom matriks, asumsi N integer tidak negatif
M = int(input("Masukkan M: "))                                                  # menerima input jumlah baris dan kolom matriks, asumsi M integer tidak negatif dan M!=N

A = [[0 for i in range(M)] for j in range(N)]                                   # membuat matriks A (NxN) berisi angka satu

for i in range(N):                                                              # perulangan untuk setiap elemen dalam matriks A selain baris dan kolom pertama
  for j in range(M):
    if diagonal(i,j,N,M) == True:
      A[i][j] = 1                                                               # jika kotak elemen dilewati diagonal, elemen = 1
    elif diagonal(i,j,N,M) == False:
      A[i][j] = 0                                                               # jika kotak elemen tidak dilewati diagonal, elemen = 0

print("Matriks hasil:")                                                         # cetak hasil
for i in range(N):                                                              # perulangan untuk setiap elemen dalam matriks A
  for j in range(M):
    print(str(A[i][j]), end=" ")                                                # cetak tiap elemen dan sambung elemen berikutnya
  print()                                                                       # buat line baru untuk baris baru