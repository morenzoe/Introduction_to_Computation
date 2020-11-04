#NIM/Nama     : 16520002/Eraraya Morenzo Muten
#Shift/Kelas  : 3.1/a
#Tanggal      : 21 Oktober 2020
#Deskripsi    : program ini akan menghitung koefisien dan eksponen hasil operasi integral dari persamaan linear. 

#Soal 2

#Program Integral ax + b

#Kamus
#a : integer
#b : integer

#Algoritma
#assign variabel a dan b dengan koefisien dan konstanta persamaan f(x) berupa bilangan positif atau negatif
a = int(input("Masukkan a: "))
b = int(input("Masukkan b: "))


#secara umum persamaan F(x) adalah (a/2)x^2 + bx
#assign ulang variabel, hitung koefisien yang berubah agar lebih mudah
a = a/2

#mencetak hasil
if a == 1: #jika koefisien a = 1
  print("Integral dari f(x) adalah x^2+" + str(b) + "x+C")

else: #jika koefisien a bukan 1
  if a%2 == 0: #jika a bilangan bulat
    print("Integral dari f(x) adalah " + str(int(a)) + "x^2" + "+" + str(b) + "x+C")
  elif a%2 == 1: #jika a bilangan desimal
    print("Integral dari f(x) adalah " + str(a) + "x^2" + "+" + str(b) + "x+C")