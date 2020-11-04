# NIM/Nama	  	: 16520002/Eraraya Morenzo Muten
# Tanggal	  	  : 4 November 2020
# Shift/Kelas	  : 3.1/a
# Deskripsi		  : Program yang mencetak kata "Siap", "Bang", dan "Jago"
#                 sesuai dengan pembagian bilangan dari 1 sampai N

# Soal 1

# Program Cetak Siap Bang Jago

#KAMUS
# N, A, B, C, x : integer

#ALGORITMA
N = int(input("Masukkan nilai N: "))      #menerima input dari user
A = int(input("Masukkan nilai A: "))      #mengecek 1 sampai N, asumsi N>=1
B = int(input("Masukkan nilai B: "))
C = int(input("Masukkan nilai C: "))

for x in range(1, N+1):                   #perulangan dari 1 sampai N
  if x%A==0:                              #percabangan
    print("Siap", end="")                 #cetak kata sesuai
  if x%B==0:
    print("Bang", end="")
  if x%C==0:
    print("Jago", end="")
  if x%A!=0 and x%B!=0 and x%C!=0:
    print(str(x), end="")
  print(" ", end="")                      #tambah spasi setiap x selesai diperiksa