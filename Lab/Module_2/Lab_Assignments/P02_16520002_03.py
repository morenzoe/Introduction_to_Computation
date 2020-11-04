# NIM/Nama	  	: 16520002/Eraraya Morenzo Muten
# Tanggal	  	  : 4 November 2020
# Shift/Kelas	  : 3.1/a
# Deskripsi		  : Program yang mencetak pola persegi angka sesuai input N

# Soal 3

# Program Cetak Pola

#KAMUS
# N, x, y : integer

#ALGORITMA
N = int(input("Masukkan bilangan: "))      #menerima input dari user

for y in range(N):                         #perulangan setengah bagian pertama
  out = ""                                 #membuat string kosong untuk tiap baris baru
  for x in range(N):                       #periksa posisi tiap pola
    if x<=y:                                
      out = out + str(x)[-1]               #pilih nilai terkecil antara absis atau ordinat
    elif y<=x:
      out = out + str(y)[-1]
  print(out + out[::-1])                   #lengkapi kalimat dengan inverse string

for y in range(N-1, -1, -1):               #ulangi proses di atas, namun terbalik urutan kalimatnya
  out = ""
  for x in range(N-1, -1 , -1): 
    if x<=y:
      out = out + str(x)[-1]
    elif y<=x:
      out = out + str(y)[-1]
  print(out[::-1] + out)                   #balik penggabungan kalimat