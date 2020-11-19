# NIM/Nama	  	: 16520002/Eraraya Morenzo Muten
# Tanggal	  	  : 18 November 2020
# Shift/Kelas	  : 3.1/a
# Deskripsi		  : Program yang mencetak sesuai dengan indeks yang diberikan
#                 untuk memcahkan kode

# Soal 2

# Program Terjemah Petunjuk Harta Karun

#KAMUS
# N : integer
# M : string
# K : array of integer


#ALGORITMA
K = [" ", "A", "B", "E", "I", "K", "L", "R", "T", "U"]

N = int(input("Masukkan banyaknya bilangan: "))                                 # deklarasi variabel N untuk jumlah bilangan

M = input("Masukkan bilangan: ")                                                # deklarasi variabel M untuk bilangan sandi, tetap dalam tipe string
                                                                                # asumsi N == M, N dan M integer positif


for i in range(N):                                                              # cetak hasil terjemahan sandi sebanyak N huruf
  print(K[int(M[i])], end="")                                                   # ambil huruf di array K sesuai dengan index dari M