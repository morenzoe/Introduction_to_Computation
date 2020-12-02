# NIM/Nama	  	: 16520002/Eraraya Morenzo Muten
# Tanggal	  	  : 02 Desember 2020
# Shift/Kelas	  : 3.1/A
# Deskripsi		  : Program yang menghitung jarak total yang harus ditempuh dengan 
# menarik garis lurus antar titik koordinat

# Soal 1

# Program Cari Jarak

# KAMUS
# A : integer
# B : array of integer

# KAMUS LOKAL
# x1, x2, y1, y2, Dx, Dy : integer
# miring : float

def pythagoras(x1, x2, y1, y2):                                                 # fungsi untuk mencari jarak jarak dua titik (sisi miring pythagoras)
# ALGORITMA
  Dx = abs(x1-x2)                                                               # selisih ordinat
  Dy = abs(y1-y2)                                                               # selisih absis
  miring = (Dx*Dx + Dy*Dy)**(1/2)                                               
  return miring

# ALGORITMA
A = int(input("Masukkan jumlah kota: "))                                        # menerima input jumlah kota, asumsi A integer tidak negatif

B = [[0 for i in range(2)] for j in range(A)]                                   # matriks untuk menyimpan titik-titik koordinat

for i in range(A):                                                              # perulangan untuk setiap elemen di dalam matriks
  for j in range(2):                                     
    if j%2 == 0:                                                                # untuk tiap baris, pertama diminta input x, kemudian y
      B[i][j] = int(input("Masukkan koordinat x kota ke "+str(i+1)+": "))       # asumsi koordinat x integer
    elif j%2 == 1:
      B[i][j] = int(input("Masukkan koordinat y kota ke "+str(i+1)+": "))       # asumsi koordinat y integer

jarak = 0                                                                       # inisiasi total jarak
for i in range(A-1):                                                            # lakukan perhitungan jarak sebanyak kota dikurang satu
  jarak += pythagoras(B[i][0], B[i+1][0], B[i][1], B[i+1][1])                   # jumlahkan total jarak dengan hasil perhitungan fungsi
    

print("Jarak totalnya "+str(jarak))                                             # cetak hasil akhir