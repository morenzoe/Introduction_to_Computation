# NIM/Nama	  	: 16520002/Eraraya Morenzo Muten
# Tanggal	  	  : 02 Desember 2020
# Shift/Kelas	  : 3.1/A
# Deskripsi		  : Program yang memeriksa jumlah bilangan positif matriks

# Soal 2

# Program Pencari Positif

#KAMUS
# N, M : integer
# A : array of integer

#ALGORITMA
N = int(input("Masukkan jumlah baris matriks: "))                               # menerima input jumlah baris matriks, asumsi N integer tidak negatif
M = int(input("Masukkan jumlah kolom matriks: "))                               # menerima input jumlah kolom matriks, asumsi M integer tidak negatif

A = [[0 for i in range(M)] for j in range(N)]                                   # membuat matriks A (MxN) berisi angka nol

for i in range(N):                                                              # perulangan untuk setiap elemen dalam matriks A
  for j in range(M):
    A[i][j] = input("Masukkan nilai A["+str(i+1)+"]["+str(j+1)+"]: ")           # menerima input elemen matriks, asumsi input string hanya simbol (*) atau (.)

for i in range(N):                                                              # perulangan untuk setiap elemen dalam matriks A
  for j in range(M):
    if A[i][j] == ".":                                                          # jika elemen bukan bom (*), periksa mata angin sejumlah sesuai lokasi masing-masing 
      count = 0
      if i == 0 and j == 0:                                                     # lokasi pojok atas kiri
        if A[i+1][j] == "*":                                                    # cek arah bawah
          count+=1
        if A[i][j+1] == "*":                                                    # cek arah kanan
          count+=1
        if A[i+1][j+1] == "*":                                                  # cek arah bawah kanan
          count+=1

      elif i == N-1 and j == 0:                                                 # lokasi pojok bawah kiri
        if A[i-1][j] == "*":                                                    # cek arah atas
          count+=1
        if A[i][j+1] == "*":                                                    # cek arah kanan
          count+=1
        if A[i-1][j-1] == "*":                                                  # cek arah atas kanan
          count+=1

      elif i == 0 and j == M-1:                                                 # lokasi pojok atas kanan
        if A[i+1][j] == "*":                                                    # cek arah bawah
          count+=1
        if A[i][j-1] == "*":                                                    # cek arah kiri
          count+=1
        if A[i+1][j-1] == "*":                                                  # cek arah bawah kiri
          count+=1

      elif i == N-1 and j == M-1:                                               # lokasi pojok bawah kanan
        if A[i-1][j] == "*":                                                    # cek arah atas
          count+=1
        if A[i][j-1] == "*":                                                    # cek arah kiri
          count+=1
        if A[i-1][j-1] == "*":                                                  # cek arah atas kiri
          count+=1
 
      elif i == 0:                                                              # lokasi sisi atas
        if A[i+1][j] == "*":                                                    # cek arah bawah
          count+=1
        if A[i][j+1] == "*":                                                    # cek arah kanan
          count+=1
        if A[i][j-1] == "*":                                                    # cek arah kiri
          count+=1
        if A[i+1][j+1] == "*":                                                  # cek arah bawah kanan
          count+=1
        if A[i+1][j-1] == "*":                                                  # cek arah bawah kiri
          count+=1

      elif i == N-1:                                                            # lokasi sisi bawah
        if A[i-1][j] == "*":                                                    # cek arah atas
          count+=1
        if A[i][j+1] == "*":                                                    # cek arah kanan
          count+=1
        if A[i][j-1] == "*":                                                    # cek arah kiri
          count+=1
        if A[i-1][j-1] == "*":                                                  # cek arah atas kanan
          count+=1
        if A[i-1][j-1] == "*":                                                  # cek arah atas kiri
          count+=1

      elif j == 0:                                                              # lokasi sisi kiri
        if A[i+1][j] == "*":                                                    # cek arah bawah
          count+=1
        if A[i][j+1] == "*":                                                    # cek arah kanan
          count+=1
        if A[i-1][j] == "*":                                                    # cek arah atas
          count+=1
        if A[i-1][j+1] == "*":                                                  # cek arah atas kanan
          count+=1
        if A[i+1][j+1] == "*":                                                  # cek arah bawah kanan
          count+=1

      elif j == M-1:                                                            # lokasi sisi kanan
        if A[i+1][j] == "*":                                                    # cek arah bawah
          count+=1
        if A[i][j-1] == "*":                                                    # cek arah kiri
          count+=1
        if A[i-1][j] == "*":                                                    # cek arah atas
          count+=1
        if A[i-1][j-1] == "*":                                                  # cek arah atas kiri
          count+=1
        if A[i+1][j-1] == "*":                                                  # cek arah bawah kiri
          count+=1

      else:                                                                     # lokasi bagian dalam
        if A[i+1][j] == "*":                                                    # cek arah bawah
          count+=1
        if A[i][j+1] == "*":                                                    # cek arah kanan
          count+=1
        if A[i][j-1] == "*":                                                    # cek arah kiri
          count+=1
        if A[i-1][j] == "*":                                                    # cek arah atas
          count+=1
        if A[i-1][j-1] == "*":                                                  # cek arah atas kiri
          count+=1
        if A[i+1][j-1] == "*":                                                  # cek arah bawah kiri
          count+=1
        if A[i-1][j+1] == "*":                                                  # cek arah atas kanan
          count+=1
        if A[i+1][j+1] == "*":                                                  # cek arah bawah kanan
          count+=1

      A[i][j] = count

for i in range(N):                                                              # perulangan untuk setiap elemen dalam matriks A
  for j in range(M):
    if A[i][j] == "*":                                                          # jika elemen adalah bom (*), ubah jadi simbol (#)
      A[i][j] = "#"

for i in range(N):                                                              # perulangan untuk setiap elemen dalam matriks A
  for j in range(M):
    if j+1 < M:                                                                 # untuk tiap elemen pada indeks kolom selain kolom terakhir
      print(str(A[i][j]), end="")                                               # cetak tiap elemen dan sambung elemen berikutnya
    elif j+1 == M:                                                              # untuk elemen pada indeks kolom terakhir
      print(str(A[i][j]))                                                       # cetak elemen tersebut dan lanjut ke line berikutnya