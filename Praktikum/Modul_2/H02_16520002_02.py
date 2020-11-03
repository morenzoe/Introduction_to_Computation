# NIM/Nama		: 16520002/Eraraya Morenzo Muten
# Tanggal		  : 1 November 2020
# Shift/Kelas	: 3.1/a
# Deskripsi		: program ini akan mencetak angka 10^x 
#               yang lebih besar dari input N

# Soal 2

# Program Cetak 10^x

#KAMUS
# N = integer
# x = integer

#ALGORITMA
N = int(input("Masukkan N: "))            #menerima input jumlah bilangan
                                          #asumsi N adalah bilangan tidak negatif
x = 0                                     #variabel pangkat
while 10**x <= N:                         #mengulang selama belum lebih dari N
  x+=1                                    #menguji x berikutnya

print(10**x)                              #mencetak hasil