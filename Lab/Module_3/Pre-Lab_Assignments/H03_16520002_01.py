# NIM/Nama	  	: 16520002/Eraraya Morenzo Muten
# Tanggal	  	  : 17 November 2020
# Shift/Kelas	  : 3.1/a
# Deskripsi		  : Program yang mencetak bilangan dengan
#                 urutan terbalik

# Soal 1

# Program Cetak Mundur

# KAMUS
# N : integer
# a : array

# ALGORITMA
N = int(input("Masukkan N: "))                                                  # buat variabel untuk menyimpan jumlah angka dari input

a = [0 for i in range(N)]                                                       # deklarasi variabel array berisi angka 0 sebanyak N

for i in range(N):                                                              # lakukan perulangan sebanyak N kali
  a[i] = int(input())                                                           # ganti isi array ke-i dengan input, asumsi input adalah bilangan bulat

print("Hasil dibalik:")

for i in range(N-1, -1, -1):                                                    # lakukan perulangan sebanyak N kali, tetapi menghitung mundur
  print(a[i])                                                                   # cetak isi array mulai dari urutan terakhir