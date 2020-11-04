# NIM/Nama	  	: 16520002/Eraraya Morenzo Muten
# Tanggal	  	  : 4 November 2020
# Shift/Kelas	  : 3.1/a
# Deskripsi		  : Program yang mencari FPB dari 4 bilangan

# Soal 2

# Program Cetak Siap Bang Jago

#KAMUS
# satu, dua, tiga, empat, i, n: integer

#ALGORITMA
satu = int(input("Masukkan bilangan pertama: "))                                #menerima input dari user
dua = int(input("Masukkan bilangan kedua: "))                                   #4 bilangan bulat positif
tiga = int(input("Masukkan bilangan ketiga: "))
empat = int(input("Masukkan bilangan keempat: "))

t = satu                                                                        #mencari nilai terkecil dari 4 bilangan
if dua<t:
  t = dua
elif tiga<t:
  t = tiga
elif empat<t:
  t = empat

for i in range(1, t+1):                                                         #perulangan dari 1 sampai nilai terkecil
  if satu%i==0:
    if dua%i==0:
      if tiga%i==0:
        if empat%i==0:                                                          #jika keempat bilangan habis dibagi i
          n=i                                                                   #nilai FPB nya adalah i

print("FPB dari keempat bilangan tersebut adalah", n)                           #cetak hasil