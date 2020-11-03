# NIM/Nama		: 16520002/Eraraya Morenzo Muten
# Tanggal	  	: 1 November 2020
# Shift/Kelas	: 3.1/a
# Deskripsi		: program ini akan memeriksa apakah bilangan X 
#               adalah bilangan prima 

# Soal 3

# Program Pemeriksa Bilangan Prima

#KAMUS
# X = integer
# i = integer

#ALGORITMA

X = int(input("Masukkan X: "))            #menerima input jumlah bilangan
                                          #asumsi X >= 2
i = 2                                     #variabel pembagi

while X%i != 0 and i<X//2:                #mengulang selama X tidak habis terbagi
  i+=1                                    #menguji i berikutnya
                                          #cukup memeriksa hingga X/2 karena selebihnya juga tidak akan bisa membagi

if i == X//2:                             #jika tidak ada bilangan lain yang dapat membagi
  print(X, "adalah bilangan prima")       #mencetak hasil prima
else:
  print(X, "bukan bilangan prima")        #mencetak hasil tidak prima