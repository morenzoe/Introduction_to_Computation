# NIM/Nama	  	: 16520002/Eraraya Morenzo Muten
# Tanggal	  	  : 17 November 2020
# Shift/Kelas	  : 3.1/a
# Deskripsi		  : Program yang memeriksa apakah suatu kata dibaca dengan cara yang sama
#                 meskipun dibalik

# Soal 3

# Program Cek Palindorm

#KAMUS
# N : integer
# k : string
# D, B : array

#ALGORITMA
N = int(input("Masukkan N: "))                                                  # buat variabel untuk menyimpan jumlah angka dari input

k = input("Masukkan string: ")                                                  # buat variabel untuk menyimpan kata, asumsi jumlah huruf sama dengan N

D = [0 for i in range(N)]                                                       # deklarasi variabel array dibaca dari depan berisi angka 0 sebanyak N

B = [0 for i in range(N)]                                                       # deklarasi variabel array dibaca dari balik berisi angka 0 sebanyak N


for i in range(N):                                                              # untuk setiap huruf pada kata
  D[i] = k[i]                                                                   # assign tiap elemen sesuai dengan huruf pada kata
  B[i] = k[N-1-i]                                                               # assign tiap elemen sesuai dengan huruf pada kata dengan urutan terbalik

if D==B:                                                                        # jika array depan dan array balik sama, kata input adalah palindrom
  print(k + " adalah palindrom")                                                # asumsi string kosong adalah palindrom
else:                                                                           # jika array depan dan array balik berbeda, kata input bukan palindrom
  print(k + " bukan palindrom")