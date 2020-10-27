#NIM/Nama     : 16520002/Eraraya Morenzo Muten
#Shift/Kelas  : 3.1/a
#Tanggal      : 21 Oktober 2020
#Deskripsi    : Program ini akan menghitung jarak tiap pilihan, memilih yang terpendek, dan menjumlahkan jaraknya.

#Soal 3

#Program Perjalanan Terpendek

#Kamus
#x1 : integer
#y1 : integer
#x2 : integer
#y2 : integer
#x3 : integer
#y3 : integer
#j1 : integer
#j2 : integer
#hs : integer

#Algoritma
#assign variabel dengan koordinat bilangan bulat positif atau negatif masing-masing lokasi
x1 = int(input("Masukkan x1: "))
y1 = int(input("Masukkan y1: "))
x2 = int(input("Masukkan x2: "))
y2 = int(input("Masukkan y2: "))
x3 = int(input("Masukkan x3: "))
y3 = int(input("Masukkan y3: "))

#menghitung jarak dari Tuan Mor ke Tuan Kin
j1 = abs(x1) + abs(y1)
#menghitung jarak dari Tuan Mor ke Tuan Ryo
j2 = abs(x2) + abs(y2)


#menentukan jarak terpendek antara Tuan Kin dan Tuan Ryo
#Jika jaraknya sama, kedua percabangan di bawah hasilnya sama. Sehingga pilih salah satu saja.
if j1 >= j2: #jika Tuan Ryo lebih dekat atau jika jaraknya sama
  #hitung hasil
  hs = abs(x2) + abs(y2) + abs(x1-x2) + abs(y1-y2) + abs(x3-x1) + abs(y3-y1)
elif j1 < j2: #jika Tuan Kin lebih dekat
  #hitung hasil
    hs = abs(x1) + abs(y1) +abs(x2-x1) + abs(y2-y1) + abs(x3-x2) + abs(y3-y2)

#mencetak hasil
print("Jarak terpendeknya adalah", hs)