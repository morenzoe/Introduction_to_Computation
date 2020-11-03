# NIM/Nama		: 16520002/Eraraya Morenzo Muten
# Tanggal		: 1 November 2020
# Shift/Kelas	: 3.1/a
# Deskripsi		: program ini akan mencetak angka 
#               dari 1 sampai N dalam satu baris

# Soal 1

# Program Cetak Angka

#KAMUS
# N = integer
# out = string

#ALGORITMA
N = int(input("Masukkan N: "))    #menerima input jumlah bilangan
                                  #asumsi input N>=1
out = "1"                         #memulai kalimat dari 1

for i in range(2, N+1):           #perulangan
  out = out + " " + str(i)        #menambahkan spasi dan angka berikutnya

print(out)                        #menampilkan kalimat