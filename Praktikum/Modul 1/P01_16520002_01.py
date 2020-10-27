#NIM/Nama     : 16520002/Eraraya Morenzo Muten
#Shift/Kelas  : 3.1/a
#Tanggal      : 21 Oktober 2020
#Deskripsi    : program ini akan menjumlahkan 4 bilangan dan membaginya dengan 4 kemudian dibulatkan ke bawah. 

#Soal 1

#Program Pembagi Permen

#Kamus
#a : integer
#b : integer
#c : integer
#d : integer


#Algoritma
#assign tiap variabel dengan jumlah permen masing-masing anak berupa bilangan bulat positif
a = int(input("Masukkan nilai a: "))
b = int(input("Masukkan nilai b: "))
c = int(input("Masukkan nilai c: "))
d = int(input("Masukkan nilai d: "))

#cetak hasil pembagian rata
print("Setiap anak akan mendapat", (a+b+c+d)//4, "permen.")